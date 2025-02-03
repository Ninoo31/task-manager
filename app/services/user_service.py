from app.models.User import User
from sqlalchemy.orm import Session
from app.config.database import SessionLocal



def register_user(username, email, password, role, session):
    if session.query(User).filter_by(username=username).first():
        return "Username already taken", False
    if session.query(User).filter_by(email=email).first():
        return "Email already registered", False

    new_user = User(username=username, email=email, role=role)
    new_user.set_password(password)
    session.add(new_user)
    session.commit()
    return new_user, True

def authenticate_user(username, password):
    session = SessionLocal()
    user = session.query(User).filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None
