from app.models import db, User

def register_user(username, email, password):
    if User.query.filter_by(username=username).first():
        return "Username already taken", False
    if User.query.filter_by(email=email).first():
        return "Email already registered", False

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user, True

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None
