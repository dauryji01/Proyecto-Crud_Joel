from flask import render_template
from app import db
from app.models import Suplemento


def configurar_rutas(app):

    @app.route("/")
    def inicio():
        suplementos = Suplemento.query.all()

        return render_template(
            "index.html",
            suplementos=suplementos
        )