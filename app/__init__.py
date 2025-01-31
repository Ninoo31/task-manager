from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
from app.models.Task import db
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt = JWTManager(app)
    db.init_app(app)
    register_blueprints(app)
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)