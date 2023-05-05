import requests
import pytest
import json
from main import fibonacci, helloFastApi, verificar_primo

expected_primo_response_false = {"validacion": "Solicitud Exitosa", "respuesta": False}
expected_primo_response_true = {"validacion": "Solicitud Exitosa", "respuesta": True}

test_data = [(0, expected_primo_response_false), (1, expected_primo_response_false), (5, expected_primo_response_true)]


@pytest.mark.parametrize("num, expected", test_data)
def test_endpoint_isPrime(num, expected):
    response = requests.get(f'http://localhost:8000/isPrime/{num}')
    data = json.loads(response.content)
    assert data == expected

def test_primo():
    assert verificar_primo(5) == {'respuesta': True, 'validacion': 'Solicitud Exitosa'}

def test_no_primo():
    assert verificar_primo(6) == {'respuesta': False, 'validacion': 'Solicitud Exitosa'}

def test_fibonacci():
    assert fibonacci(5) == {"respuesta": 5, "validacion": "Solicitud Exitosa"}

def test_fibonacci_exceptionManaged():
    assert fibonacci("error") == {"validacion": "Error: el valor introducido no es un numero entero"}

def test_helloFastApi():
    assert helloFastApi() == {"mensaje": "Hello FastAPI"}