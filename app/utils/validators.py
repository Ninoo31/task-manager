import re

def validate_task_data(data):
    if "title" not in data or not data["title"]:
        return "Title is required", False
    if "priority" in data and data["priority"] not in ["low", "medium", "high"]:
        return "Priority must be low, medium, or high", False
    return "", True

def validate_task_id(task_id):
    if not isinstance(task_id, int) or task_id <= 0:
        return "Invalid task ID. It must be a positive integer.", False
    return "", True

def validate_user_data(data):
    """ Valide les données avant l'inscription d'un utilisateur """
    if "username" not in data or not data["username"].strip():
        return "Username is required", False
    if len(data["username"]) < 3:
        return "Username must be at least 3 characters long", False
    if "email" not in data or not validate_email(data["email"]):
        return "Invalid email format", False
    if "password" not in data or len(data["password"]) < 6:
        return "Password must be at least 6 characters long", False
    return "", True

def validate_email(email):
    """ Vérifie si l'email a un format valide """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None
