import pytest
#ejecutar pruebas python -m pytest -v
from app import create_app, db
from app.models import Suplemento


@pytest.fixture
def app():
    app = create_app()

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        db.drop_all()
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_inicio(client):
    respuesta = client.get("/")

    assert respuesta.status_code == 200


def test_crear_suplemento(client):
    respuesta = client.post(
        "/crear",
        data={
            "nombre": "Proteína Whey",
            "marca": "Optimum Nutrition",
            "categoria": "Proteína",
            "precio": 2500,
            "cantidad": 10,
            "submit": "Guardar"
        },
        follow_redirects=True
    )

    assert respuesta.status_code == 200


def test_editar_suplemento(client, app):
    with app.app_context():
        suplemento = Suplemento(
            nombre="Creatina",
            marca="MuscleTech",
            categoria="Creatina",
            precio=1800,
            cantidad=5
        )

        db.session.add(suplemento)
        db.session.commit()

        suplemento_id = suplemento.id

    respuesta = client.post(
        f"/editar/{suplemento_id}",
        data={
            "nombre": "Creatina Monohidratada",
            "marca": "MuscleTech",
            "categoria": "Creatina",
            "precio": 2000,
            "cantidad": 8,
            "submit": "Guardar"
        }
    )

    assert respuesta.status_code == 302


def test_eliminar_suplemento(client, app):
    with app.app_context():
        suplemento = Suplemento(
            nombre="BCAA",
            marca="Universal",
            categoria="Aminoácidos",
            precio=1500,
            cantidad=4
        )

        db.session.add(suplemento)
        db.session.commit()

        suplemento_id = suplemento.id

    respuesta = client.post(f"/eliminar/{suplemento_id}")

    assert respuesta.status_code == 302