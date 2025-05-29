import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")  
    JWT_EXPIRACION_SEGUNDOS  = 3600 #una hora

class ConfigTesting:
    TESTING = True
    DB_NAME = os.getenv("DB_NAME_TEST")
    DB_USER = os.getenv("DB_USER_TEST")
    DB_PASSWORD = os.getenv("DB_PASSWORD_TEST")
    DB_HOST = os.getenv("DB_HOST_TEST")
    DB_PORT = os.getenv("DB_PORT_TEST")
    SECRET_KEY = os.getenv("SECRET_KEY")  
    JWT_EXPIRACION_SEGUNDOS  = 3600 #una hora