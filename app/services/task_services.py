from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.Task import Task

def create_task(data):
    session = SessionLocal()
    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status=data.get("status", "pending"),
        priority=data.get("priority", "low"),
        deadline=data.get("deadline")
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return new_task

def get_all_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def get_task_by_id(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    session.close()
    if not task:
        raise Exception("Task not found")
    return task

def update_task(task, data):
    session = SessionLocal()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)
    task.deadline = data.get("deadline", task.deadline)
    session.commit()
    session.refresh(task)
    session.close()
    return task

def delete_task(task):
    session = SessionLocal()
    session.delete(task)
    session.commit()
    session.close()
