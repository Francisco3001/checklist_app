from flask import g
from app.decorators.service_handler import service_handler
from app.schema import ItemCreateSchema, ItemUpdateSchema, ItemDeleteSchema
from database.db import db_execute, db_fetchall, db_fetchone


@service_handler(schema_class=ItemCreateSchema)
def post_items_service(data):
    '''
    crea la tarea y la agrega a la bdd
    '''
    
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    id_usuario = g.usuario_id

    query = """
        INSERT INTO Items (id_usuario, nombre, descripcion)
        VALUES (%s, %s, %s)
        RETURNING *
    """
    db_execute(query, id_usuario, nombre, descripcion)
    return {"message": "Item creado exitosamente"}, 201

@service_handler(schema_class=None)
def get_items_service(data):
    '''
    devuelve todas las tareas de la bdd del usuario autenticado
    '''
    id_usuario = g.usuario_id
    query = """
        SELECT * FROM Items
        WHERE id_usuario = %s
        ORDER BY fecha_creacion DESC
    """
    items = db_fetchall(query, id_usuario)

    return {"items": items}, 200


@service_handler(schema_class=ItemUpdateSchema)
def put_items_service(data):
    '''
    modifica una tarea si pertenece al usuario autenticado
    puede modificar nombre, descripcion y completado
    '''
    
    id_item = data.get("id_item")
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")  
    completado = data.get("completado")  
    id_usuario = g.usuario_id

    query_check = "SELECT * FROM Items WHERE id = %s AND id_usuario = %s"
    item = db_fetchone(query_check, id_item, id_usuario)

    if not item:
        return {"error": "Item no encontrado o no autorizado"}, 404

    query_update = """
        UPDATE Items
        SET nombre = %s,
            descripcion = %s,
            completado = %s
        WHERE id = %s
    """

    db_execute(query_update, nombre, descripcion, completado, id_item)

    return {"message": "Item actualizado correctamente"}, 200


@service_handler(schema_class=ItemDeleteSchema)
def delete_items_service(data):
    '''
    elimina una tarea de la bdd si pertenece al usuario autenticado
    '''
    id_usuario = g.usuario_id
    item_id = data.get("id_item")

    query_check = """
        SELECT * FROM Items
        WHERE id = %s AND id_usuario = %s
    """
    item = db_fetchone(query_check, item_id, id_usuario)

    if not item:
        return {"error": "Item no encontrado o no autorizado"}, 404

    query_delete = "DELETE FROM Items WHERE id = %s"
    db_execute(query_delete, item_id)

    return {"message": "Item eliminado correctamente"}, 200


