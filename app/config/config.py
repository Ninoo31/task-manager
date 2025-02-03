import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Charger les variables d'environnement
load_dotenv()

# Base directory : Toujours pointer vers la racine du projet
#BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  
#DATABASE_PATH = os.path.join(BASE_DIR, "tasks.db")  # ✅ Fichier DB dans la racine du projet

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Expiration en secondes (1 heure)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
