import os
from flask import Flask
from config import Config
from models import db, Task  # Import des modèles

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Initialisation de SQLAlchemy
    return app

app = create_app()

# Vérifier si la base existe avant de la créer
if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists("tasks.db"):  # Vérifie si la base existe déjà
            print("🔍 Création de la base de données...")
            db.create_all()
            print("✅ Base et tables créées avec succès !")
        else:
            print("✅ La base de données existe déjà.")

    # ⚠️ Désactiver le reloader pour éviter le double démarrage
    app.run(debug=True, use_reloader=False)
