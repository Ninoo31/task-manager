from flask_jwt_extended import jwt
from flask import jsonify

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401
