import unittest
from fastapi.testclient import TestClient
from src.main import app


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_generate(self):
        with open('src/api/file.csv', 'rb') as f:
            response = self.app.post('/api/v1/generate', files={'file':f})
            self.assertEqual(response.status_code, 200)

    def test_send_queue(self):
        response = self.app.get('/api/v1/send_mq')
        self.assertTrue(response.content)
