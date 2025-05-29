from functools import wraps
from marshmallow import ValidationError, RAISE
import psycopg2 

def service_handler(schema_class=None):
    def decorator(func):
        @wraps(func)
        def wrapper(data=None, *args, **kwargs):
            try:
                if schema_class:
                    data = schema_class().load(data or {}, unknown=RAISE)
                
                return func(data, *args, **kwargs)
            
            except ValidationError as err:
                return {
                    "error": "Datos inválidos",
                    "detalles": err.messages
                }, 400

            except psycopg2.Error as err:
                print(f"[DB ERROR] {err.pgcode}: {err.pgerror}")
                return {
                    "error": "Error de base de datos",
                    "detalles": str(err)
                }, 500

            except Exception as err:
                return {
                    "error": "Error interno",
                    "detalles": str(err)
                }, 500

        return wrapper
    return decorator