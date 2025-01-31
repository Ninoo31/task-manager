import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Récupère le chemin absolu du projet
DATABASE_PATH = os.path.join(BASE_DIR, "tasks.db")  # Fichier DB dans le dossier du projet

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # Active les logs SQL
