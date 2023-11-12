import requests
import unittest


class ApiTest(unittest.TestCase):
    def test_generate(self):
        with open('src/api/departuredelays.csv', 'rb') as f:
            response = requests.post(url='http://127.0.0.1:5049/api/v1/generate', files={'file': f})
            self.assertEqual(response.status_code, 200)

    def test_download(self):
        response = requests.get('http://127.0.0.1:5049/api/v1/download')
        self.assertTrue(response.content)

    def test_send_queue(self):
        response = requests.get('http://127.0.0.1:5049/api/v1/send_mq')
        self.assertTrue(response.content)

