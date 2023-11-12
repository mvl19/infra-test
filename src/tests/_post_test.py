import requests


def make_rq():
    with open('../api/departuredelays.csv', 'rb') as f:
        response = requests.post(url='http://127.0.0.1:5049/generate/', files={'file': f})
        return response.content, response.status_code


def test_post():
    with open('../api/departuredelays.csv', 'rb') as f:
        response = requests.post(url='http://127.0.0.1:5049/generate/', files={'file': f})
        assert response.status_code == 200

