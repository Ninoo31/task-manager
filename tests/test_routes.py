import unittest
from app import app, db
from app.models.Task import Task

class TaskRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.app.post("/tasks/", json={"title": "Test Task", "priority": "medium"})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        response = self.app.get("/tasks/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
