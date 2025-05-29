from marshmallow import Schema, fields, validate


class ItemCreateSchema(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    descripcion = fields.Str(required=True, validate=validate.Length(min=1))


class ItemUpdateSchema(Schema):
    id_item = fields.Int(required=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    descripcion = fields.Str(required=True, validate=validate.Length(min=1))
    completado = fields.Bool(required=True)


class ItemDeleteSchema(Schema):
    id_item = fields.Int(required=True)

class LoginSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1))
    contraseña = fields.Str(required=True, validate=validate.Length(min=1))

class RegisterSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1))
    contraseña = fields.Str(required=True, validate=validate.Length(min=1))
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    apellido = fields.Str(required=True, validate=validate.Length(min=1))
