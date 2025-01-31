from models import db, Task

def create_task(data):
    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status=data.get("status", "pending"),
        priority=data.get("priority", "low"),
        deadline=data.get("deadline")
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get_or_404(task_id)

def update_task(task, data):
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)
    task.deadline = data.get("deadline", task.deadline)
    db.session.commit()
    return task

def delete_task(task):
    db.session.delete(task)
    db.session.commit()
