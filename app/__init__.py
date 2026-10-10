from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


db = SQLAlchemy() # Herramienta para trabajar con la base de datos  
migrate = Migrate()


def create_app():
    app = Flask(__name__) # Crea la aplicación web con Flask
    app.config.from_object(Config) # Llamar la configuracion

#iniciae base de datos y migración
    db.init_app(app)
    migrate.init_app(app, db)

#llamar modelos
    from app import models

#LLama a las rutas de la aplicación ya configurada
    from app.routes import configurar_rutas
    configurar_rutas(app)

    with app.app_context():
        db.create_all()
    return app