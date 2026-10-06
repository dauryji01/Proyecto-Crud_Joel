from flask import render_template
from app import db
from app.models import Suplemento
from app.forms import SuplementoForm


def configurar_rutas(app):

    @app.route("/")
    def inicio():
        suplementos = Suplemento.query.all()

        return render_template(
            "index.html",
            suplementos=suplementos
        )

    @app.route("/crear", methods=["GET", "POST"])
    def crear():
        form = SuplementoForm()

        if form.validate_on_submit():
            suplemento = Suplemento(
                nombre=form.nombre.data,
                marca=form.marca.data,
                categoria=form.categoria.data,
                precio=form.precio.data,
                cantidad=form.cantidad.data
            )

            db.session.add(suplemento)
            db.session.commit()

            return "Suplemento creado correctamente"

        return render_template("crear.html", form=form)

    @app.route("/editar/<int:id>", methods=["GET", "POST"])
    def editar(id):
        suplemento = Suplemento.query.get_or_404(id)
        form = SuplementoForm(obj=suplemento)

        if form.validate_on_submit():
            suplemento.nombre = form.nombre.data
            suplemento.marca = form.marca.data
            suplemento.categoria = form.categoria.data
            suplemento.precio = form.precio.data
            suplemento.cantidad = form.cantidad.data

            db.session.commit()

            return "Suplemento actualizado correctamente"

        return render_template(
            "editar.html",
            form=form,
            suplemento=suplemento
        )

    @app.route("/eliminar/<int:id>", methods=["POST"])
    def eliminar(id):
        suplemento = Suplemento.query.get_or_404(id)

        db.session.delete(suplemento)
        db.session.commit()

        return "Suplemento eliminado correctamente"        