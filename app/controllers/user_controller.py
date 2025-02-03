from flask import request, jsonify
from app.services.user_service import register_user, authenticate_user
from app.config.database import SessionLocal
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.User import User
from app.utils.validators import validate_user_data

def handle_register():
    # On crée et gère la session avec un gestionnaire de contexte pour garantir sa fermeture
    with SessionLocal() as session:
        data = request.get_json()

        # Vérifier la validité des données
        error, valid = validate_user_data(data)
        if not valid:
            return jsonify({"error": error}), 400

        # Récupérer le rôle, sinon "user" par défaut
        role = data.get("role", "user")
        if role not in ["user", "admin"]:
            return jsonify({"error": "Invalid role"}), 400

        # Vérifier si l'email ou le username existent déjà
        existing_user = session.query(User).filter(
            (User.username == data["username"]) | (User.email == data["email"])
        ).first()
        if existing_user:
            return jsonify({"error": "Username or email already exists"}), 400

        # Enregistrer le nouvel utilisateur en passant la session créée
        user, success = register_user(data["username"], data["email"], data["password"], role, session)
        if not success:
            return jsonify({"error": user}), 400

        # Ici, l'instance user est toujours liée à la session active
        print("User's role: " + user.role)
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
    session = SessionLocal()
    """ Récupérer les informations de l'utilisateur connecté """
    user_id = get_jwt_identity()  # Récupère l'ID depuis le token JWT
    user = session.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role
    })