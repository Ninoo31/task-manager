from flask import Flask, request, jsonify
from app.config import Config
from app.models import db, Task
from services.task_services import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    return app

app = create_app()

# Routes API CRUD
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = create_task(data)
    return jsonify({"message": "Task created successfully!", "task_id": new_task.id}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{ "id": task.id, "title": task.title, "description": task.description, "status": task.status, "priority": task.priority, "deadline": task.deadline } for task in tasks])

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)
    task.deadline = data.get("deadline", task.deadline)
    db.session.commit()
    return jsonify({"message": "Task updated successfully!"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
