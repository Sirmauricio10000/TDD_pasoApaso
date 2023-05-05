import requests
import pytest
import json

test_data_isPrime = [
    (0, False),
    (1, False),
    (5, True),
    (17,True)]

test_data_fibonacci = [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55)
]

@pytest.mark.parametrize("num, expected", test_data_isPrime)
def test_endpoint_isPrime(num, expected):
    response = requests.post(f'http://localhost:8000/isPrime/{num}')
    data = json.loads(response.content)
    assert data["respuesta"] == expected

@pytest.mark.parametrize("num, expected", test_data_fibonacci)
def test_endpoint_fibonacci(num, expected):
    response = requests.post(f'http://localhost:8000/fibonacci/{num}')
    data = json.loads(response.content)
    assert data["respuesta"] == expected