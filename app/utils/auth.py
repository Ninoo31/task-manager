from flask_jwt_extended import get_jwt_identity
from app.models.User import User
from functools import wraps
from flask import jsonify

def admin_required(fn):
    """ Décorateur pour restreindre l'accès aux admins uniquement """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user or user.role != "admin":
            return jsonify({"error": "Admin access required"}), 403

        return fn(*args, **kwargs)
    return wrapper
