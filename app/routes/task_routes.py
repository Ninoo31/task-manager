from flask import Blueprint
from controllers.task_controller import handle_create_task, handle_get_tasks, handle_update_task, handle_delete_task

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

task_bp.route("/", methods=["POST"])(handle_create_task)
task_bp.route("/", methods=["GET"])(handle_get_tasks)
task_bp.route("/<int:task_id>", methods=["PUT"])(handle_update_task)
task_bp.route("/<int:task_id>", methods=["DELETE"])(handle_delete_task)
