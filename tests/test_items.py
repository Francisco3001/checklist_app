import json

def headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def test_post_item(client, test_token):
    res = client.post("/item", headers=headers(test_token), data=json.dumps({
        "nombre": "Tarea de prueba",
        "descripcion": "Hecha con pytest"
    }))
    assert res.status_code == 201
    data = res.get_json()
    assert "message" in data

def test_get_items(client, test_token):
    res = client.get("/item", headers=headers(test_token))
    assert res.status_code == 200
    assert "items" in res.get_json()

def test_put_item(client, test_token):
    # Crear item
    client.post("/item", headers=headers(test_token), data=json.dumps({
        "nombre": "Temporal",
        "descripcion": "Editar"
    }))
    item_id = client.get("/item", headers=headers(test_token)).get_json()["items"][0]["id"]

    # Editar
    res = client.put("/item", headers=headers(test_token), data=json.dumps({
        "id_item": item_id,
        "nombre": "Actualizado",
        "descripcion": "Modificado",
        "completado": True
    }))
    assert res.status_code == 200
    assert "message" in res.get_json()

def test_delete_item(client, test_token):
    # Crear item
    client.post("/item", headers=headers(test_token), data=json.dumps({
        "nombre": "Borrar",
        "descripcion": "Temp"
    }))
    items = client.get("/item", headers=headers(test_token)).get_json()["items"]
    id_item = items[-1]["id"]

    # Borrar
    res = client.delete("/item", headers=headers(test_token), data=json.dumps({
        "id_item": id_item
    }))
    assert res.status_code == 200
    assert "message" in res.get_json()
