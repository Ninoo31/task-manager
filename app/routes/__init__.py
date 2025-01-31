from flask import Blueprint
from .task_routes import task_bp

def register_blueprints(app):
    app.register_blueprint(task_bp)
