import requests

from app import app


def test_api():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r = requests.post(f'http://127.0.0.1:5000/', json=data)
    assert r.json() == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert r.status_code == 200
