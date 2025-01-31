def validate_task_data(data):
    if "title" not in data or not data["title"]:
        return "Title is required", False
    if "priority" in data and data["priority"] not in ["low", "medium", "high"]:
        return "Priority must be low, medium, or high", False
    return "", True
