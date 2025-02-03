from flask import Flask
from flask_jwt_extended import JWTManager
#from flask_cors import CORS
from app.config.config import Config
from app.routes import register_blueprints
from app.error.jwt_error import register_jwt_errors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt = JWTManager(app)  # ✅ Initialisation de JWT
    register_jwt_errors(app)  # ✅ Enregistrement des erreurs JWT
    register_blueprints(app)
    #CORS(app)
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        app.run(debug=True, use_reloader=False)