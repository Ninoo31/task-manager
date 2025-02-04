from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.task_controller import *

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

task_bp.route("", methods=["POST"])(jwt_required()(handle_create_task))
task_bp.route("", methods=["GET"])(jwt_required()(handle_get_tasks))
task_bp.route("/user", methods=["GET"])(jwt_required()(handle_get_tasks_by_user_id))
task_bp.route("/<int:task_id>", methods=["PUT"])(jwt_required()(handle_update_task))
task_bp.route("/<int:task_id>", methods=["DELETE"])(jwt_required()(handle_delete_task))

