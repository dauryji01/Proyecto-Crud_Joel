from flask import Flask

def create_app():
    app = Flask(__name__)

    # configuración
    app.config.from_object("config")

    # rutas
    from app.routes import routes
    app.register_blueprint(routes)

    return app