
import os
from flask import jsonify
from app.decorators.service_handler import service_handler
from app.schema import LoginSchema, RegisterSchema
from app.services.jwt_service import generar_token
from database.db import db_execute, db_fetchone
import hashlib

@service_handler(schema_class=LoginSchema)
def log_in(data):
    query = 'SELECT * from usuarios where email = %s'
    user = db_fetchone(query, data["email"])

    if not user:
        return jsonify({"error": "El usuario no existe"}), 404
    
    if not check_contraseña(user["id"], data["contraseña"]):
        return jsonify({"error": "Contraseña invalida"}), 401

    token = generar_token(user["id"])
    return jsonify({"token": token})

@service_handler(schema_class=RegisterSchema)
def register(data):
    query = 'SELECT * from usuarios where email = %s'
    user = db_fetchone(query, data['email'])
    if user:
        return jsonify({"error": "Ese email ya se encuentra registrado"}), 400
    hash, salt = _hashear_contraseña(data['contraseña'])

    query = 'insert into usuarios (email, hash, salt, nombre, apellido) values (%s, %s, %s, %s, %s)'
    db_execute(query, data['email'], hash, salt, data['nombre'], data['apellido'])
    return jsonify("Usuario creado exitosamente"), 200



def _hashear_contraseña(contraseña):
    salt = os.urandom(16) 
    hash_bytes = hashlib.pbkdf2_hmac('sha256', contraseña.encode(), salt, 100000)
    hash_hex = hash_bytes.hex()
    salt_hex = salt.hex()
    return hash_hex, salt_hex


def check_contraseña(id_usuario, contraseña):
    query = 'SELECT hash, salt from usuarios WHERE id = %s'
    usuario = db_fetchone(query, id_usuario)
    salt = bytes.fromhex(usuario["salt"])
    hash_bytes = hashlib.pbkdf2_hmac('sha256', contraseña.encode(), salt, 100000)
    hash_hex = hash_bytes.hex()

    return hash_hex == usuario["hash"]