from flask import request, jsonify
from services.task_services import create_task, get_all_tasks, get_task_by_id, update_task, delete_task

def handle_create_task():
    data = request.get_json()
    task = create_task(data)
    return jsonify({"message": "Task created successfully!", "task_id": task.id}), 201

def handle_get_tasks():
    tasks = get_all_tasks()
    return jsonify([{ "id": task.id, "title": task.title, "description": task.description, "status": task.status, "priority": task.priority, "deadline": task.deadline } for task in tasks])

def handle_update_task(task_id):
    task = get_task_by_id(task_id)
    data = request.get_json()
    updated_task = update_task(task, data)
    return jsonify({"message": "Task updated successfully!"})

def handle_delete_task(task_id):
    task = get_task_by_id(task_id)
    delete_task(task)
    return jsonify({"message": "Task deleted successfully!"})
