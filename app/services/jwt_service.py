import jwt
import uuid
from datetime import datetime, timedelta
from flask import current_app, jsonify, request

def generar_token(user_id):
    '''
    Genera un token de autenticacion
    '''
    jti = str(uuid.uuid4())
    ahora = datetime.now()
    exp = ahora + timedelta(seconds=current_app.config["JWT_EXPIRACION_SEGUNDOS"])

    payload = {
        "sub": str(user_id),
        "jti": jti,
        "iat": ahora.timestamp(),
        "exp": exp.timestamp()
    }

    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

    return token

def validar_token():
    '''
    Valida el token desde Authorization header o desde cookie "token"
    '''
    token = None

    # 1. Intentar desde header Authorization (para back)
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]

    # 2. Si no hay header, intentar desde cookie (para front)
    if not token and 'token' in request.cookies:
        token = request.cookies.get("token")

    if not token:
        return jsonify({"error": "Token faltante"}), 401

    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return payload["sub"]

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401
    