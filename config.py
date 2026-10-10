import os #base de datos
    
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "DaDy123987")
    SQLALCHEMY_DATABASE_URI = "sqlite:///suplementos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

