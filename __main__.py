from fastapi import FastAPI
import uvicorn
from restaurante import Restaurante
from cliente import Cliente
from entregador import Entregador
import fila


app = FastAPI()

@app.get('/restaurante/{nome}')
def get_restaurante(nome: str):
    """
    Pedidos pendentes deste restaurante,
    mudam para o status `Preparando`
    """
    return Restaurante(nome=nome).recebe_pedidos()

@app.get('/entregador/{nome}')
def get_entregador(nome: str):
    """
    Pedidos em preparação são atribuídos ao entregador
    e mudam para o status `Em transporte`
    """
    return Entregador(nome=nome).recebe_pedidos()

@app.get('/cliente/{nome}')
def get_cliente(nome: str):
    """
    Pedidos em transporte deste cliente,
    mudam para o status `Entregue`
    """
    return Cliente(nome=nome).recebe_pedidos()

@app.get('/novo_pedido')
def novo_pedido():
    """
    Cria pedidos fictícios para testar o sistema.
    E cria as pessoas envolvidas, caso não existam.
    """
    return fila.grava_pedido()


uvicorn.run(app)
