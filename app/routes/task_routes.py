from flask import Blueprint
from app.controllers.task_controller import handle_create_task, handle_get_tasks, handle_update_task, handle_delete_task

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

# Suppression du "/" final pour éviter les redirections
task_bp.route("", methods=["POST"])(handle_create_task)  # "/tasks"
task_bp.route("", methods=["GET"])(handle_get_tasks)  # "/tasks"
task_bp.route("/<int:task_id>", methods=["PUT"])(handle_update_task)  # "/tasks/1"
task_bp.route("/<int:task_id>", methods=["DELETE"])(handle_delete_task)  # "/tasks/1"
