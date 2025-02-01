from flask import Blueprint
from app.controllers.user_controller import *

# Création du Blueprint pour les utilisateurs
user_bp = Blueprint("users", __name__, url_prefix="/users")

# Définition des routes
user_bp.route("/register", methods=["POST"])(handle_register)
user_bp.route("/login", methods=["POST"])(handle_login)
user_bp.route("/refresh", methods=["POST"])(handle_refresh)
user_bp.route("/profile", methods=["GET"])(handle_profile)