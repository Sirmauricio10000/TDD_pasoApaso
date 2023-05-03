from fastapi import FastAPI
from fastapi import FastAPI, Response

app = FastAPI(title= 'Aplicacion DDP', 
              description= 'Proyecto de pruebas de api de la asignatura DDP', 
              version='1.0')

@app.post("/isPrime/{n}")
def verificar_primo(n):
    return True