import pytest
from app import create_app
from app.services.jwt_service import generar_token
from database.db import db_execute


@pytest.fixture
def app():
    app = create_app(testing=True)
    with app.app_context():
        db_execute("DROP TABLE IF EXISTS Items")
        db_execute("DROP TABLE IF EXISTS Usuarios")

        db_execute("""
            CREATE TABLE Usuarios (
                id SERIAL PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            );
        """)

        db_execute("""
            CREATE TABLE Items (
                id SERIAL PRIMARY KEY,
                id_usuario INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT NOW(),
                completado BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
            );
        """)

        db_execute("""
            INSERT INTO Usuarios (email, hash, salt, nombre, apellido)
            VALUES ('test@user.com', 'hash', 'salt', 'Test', 'User');
        """)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_token(app):
    with app.app_context():
        return generar_token(1)

