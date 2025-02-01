from flask import jsonify
from flask_jwt_extended import JWTManager

def register_jwt_errors(app):
    """ Enregistre les erreurs JWT dans l'application Flask """

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """ Gestion des tokens expirés """
        return jsonify({
            "error": "Token has expired",
            "message": "Please refresh your token"
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        """ Gestion des tokens invalides """
        return jsonify({
            "error": "Invalid token",
            "message": "The provided token is not valid"
        }), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        """ Gestion des accès sans token """
        return jsonify({
            "error": "Token missing",
            "message": "Authorization token is required"
        }), 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        """ Gestion des tokens révoqués """
        return jsonify({
            "error": "Token revoked",
            "message": "Your token has been revoked, please login again"
        }), 401
