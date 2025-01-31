from flask import request, jsonify
from services.user_service import register_user, authenticate_user
from flask_jwt_extended import create_access_token
from models import User
from utils.validators import validate_user_data  # ✅ Import des validateurs

def handle_register():
    """ Gère l'inscription d'un utilisateur avec validation """
    data = request.get_json()

    # Vérifier la validité des données
    error, valid = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    # Vérifier si l'email ou le username existent déjà
    existing_user = User.query.filter((User.username == data["username"]) | (User.email == data["email"])).first()
    if existing_user:
        return jsonify({"error": "Username or email already exists"}), 400

    # Enregistrer le nouvel utilisateur
    user, success = register_user(data["username"], data["email"], data["password"])
    if not success:
        return jsonify({"error": user}), 400
    
    return jsonify({"message": "User registered successfully!"}), 201

def handle_login():
    """ Gère la connexion et génère un token JWT """
    data = request.get_json()
    
    user = authenticate_user(data["username"], data["password"])
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})
