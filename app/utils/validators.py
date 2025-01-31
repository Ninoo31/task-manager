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