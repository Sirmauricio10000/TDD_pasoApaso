from fastapi import FastAPI
from fastapi import FastAPI, Response

app = FastAPI(title= 'Aplicacion DDP', 
              description= 'Proyecto de pruebas de api de la asignatura DDP', 
              version='1.0')

@app.post("/isPrime/{n}")
def verificar_primo(n: str):
    response: Response
    validacion = validaciones(n, "primo")
    if validacion != "Solicitud Exitosa":
        response.status_code = 400
        return {"validacion": validacion}
    
    respuesta = es_primo(n)
    return {"validacion": validacion, "respuesta": respuesta}

@app.post("/fibonacci/{position}")
def fibonacci(position: int):

    return 5


def es_primo(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def validaciones(x, type):
    try:
        num = int(x)
    except:
        return "Error: el valor introducido no es un numero entero"
        
    if num < 0:
        return "Error: el valor introducido es negativo"
    
    if num > 1000 and type == "fibonacci":
        return "Error: El limite de la posicion es 1000"
    
    if num >= 4.3466557686937455e+208 and type == "primo":
        return "Error: El valor introducido supera el limite: 4.3466557686937455e+208"
    return "Solicitud Exitosa"