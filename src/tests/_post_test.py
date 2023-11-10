import requests


def reader():
    with open('../api/departuredelays.csv', 'rb') as f:
        return {"file": f}


def make_rq():
    with open('../api/departuredelays.csv', 'rb') as f:
        response = requests.post(url='http://127.0.0.1:5049/generate/', files={'file':f})
        return response.content, response.status_code


if __name__ == "__main__":
    print(make_rq())