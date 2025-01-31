from flask import Blueprint
from .task_routes import task_bp
from .user_routes import user_bp

def register_blueprints(app):
    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
