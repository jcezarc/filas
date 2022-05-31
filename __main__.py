from fastapi import FastAPI
import uvicorn
from restaurante import Restaurante
from cliente import Cliente
from entregador import Entregador
import fila


app = FastAPI()

@app.get('/restaurante/{nome}')
def get_restaurante(nome: str):
    return Restaurante(nome=nome).recebe_pedidos()

@app.get('/cliente/{nome}')
def get_cliente(nome: str):
    return Cliente(nome=nome).recebe_pedidos()

@app.get('/entregador/{nome}')
def get_entregador(nome: str):
    return Entregador(nome=nome).recebe_pedidos()

@app.get('/novo_pedido')
def novo_pedido():
    return fila.grava_pedido()


uvicorn.run(app)
