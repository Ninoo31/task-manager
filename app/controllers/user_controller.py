from flask import request, jsonify
from app.services.user_service import register_user, authenticate_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.User import User
from app.utils.validators import validate_user_data  # ✅ Import des validateurs

def handle_register():
    """ Gère l'inscription d'un utilisateur avec validation """
    data = request.get_json()

    # Vérifier la validité des données
    error, valid = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400
    
    role = data.get("role", "user")  # ✅ Récupérer le rôle (sinon "user" par défaut)
    if role not in ["user", "admin"]:
        return jsonify({"error": "Invalid role"}), 400

    # Vérifier si l'email ou le username existent déjà
    existing_user = User.query.filter((User.username == data["username"]) | (User.email == data["email"])).first()
    if existing_user:
        return jsonify({"error": "Username or email already exists"}), 400

    # Enregistrer le nouvel utilisateur
    user, success = register_user(data["username"], data["email"], data["password"], role)
    if not success:
        return jsonify({"error": user}), 400
    
    return jsonify({"message": "User registered successfully!", "role": user.role}), 201

def handle_login():
    """ Gère la connexion et génère un token JWT """
    data = request.get_json()
    
    user = authenticate_user(data["username"], data["password"])
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})

@jwt_required(refresh=True)  # ✅ Route protégée par un refresh token
def handle_refresh():
    """ Génére un nouveau `access_token` à partir du `refresh_token` """
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)  # ✅ Nouveau token

    return jsonify({"access_token": new_access_token})

@jwt_required()
def handle_profile():
    """ Récupérer les informations de l'utilisateur connecté """
    user_id = get_jwt_identity()  # Récupère l'ID depuis le token JWT
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role
    })