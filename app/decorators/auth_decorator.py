from functools import wraps
from flask import g

from app.services.jwt_service import validar_token

def requiere_autenticacion(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        resultado = validar_token()
        if isinstance(resultado, tuple):
            return resultado
        g.usuario_id = resultado 
        return f(*args, **kwargs)
    return wrapper
