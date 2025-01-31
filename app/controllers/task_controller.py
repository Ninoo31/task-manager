from flask import request, jsonify
from app.services.task_services import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from utils.validators import validate_task_data, validate_task_id  # Import des validateurs
from flask_jwt_extended import jwt_required  # Import du JWT pour protéger les routes

@jwt_required()
def handle_create_task():
    data = request.get_json()
    error, valid = validate_task_data(data)
    if not valid:
        return jsonify({"error": error}), 400  # Retourne une erreur HTTP 400 si les données sont invalides

    task = create_task(data)
    return jsonify({"message": "Task created successfully!", "task_id": task.id}), 201

@jwt_required()
def handle_get_tasks():
    tasks = get_all_tasks()
    return jsonify([{ "id": task.id, "title": task.title, "description": task.description, "status": task.status, "priority": task.priority, "deadline": task.deadline } for task in tasks])

@jwt_required()
def handle_update_task(task_id):
    error, valid = validate_task_id(task_id)
    if not valid:
        return jsonify({"error": error}), 400  # Vérification de l'ID de la tâche

    task = get_task_by_id(task_id)
    data = request.get_json()
    error, valid = validate_task_data(data)
    if not valid:
        return jsonify({"error": error}), 400  # Retourne une erreur HTTP 400 si les données sont invalides

    updated_task = update_task(task, data)
    return jsonify({"message": "Task updated successfully!"})

@jwt_required()
def handle_delete_task(task_id):
    error, valid = validate_task_id(task_id)
    if not valid:
        return jsonify({"error": error}), 400  # Vérification de l'ID de la tâche
    
    task = get_task_by_id(task_id)
    delete_task(task)
    return jsonify({"message": "Task deleted successfully!"})
