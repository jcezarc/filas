from dataclasses import dataclass
from mongo_table import MongoTable
from pedido import Pedido, STATUS_PENDENTE, STATUS_PREPARANDO
from fastapi import FastAPI
import uvicorn


@dataclass
class Restaurante(MongoTable):
    nome: str
    pratos: dict = {}

    def add_prato(self, nome:str, preco:float):
        self.pratos[nome] = preco
        return self

    def recebe_pedidos(self):
        busca = Pedido(restaurante=self, status=STATUS_PENDENTE)
        encontrado = busca.find()
        if encontrado:
            primeiro = encontrado.pop(0)
            pedido = Pedido(**primeiro)
            print('Preparando o pedido {}...'.format(pedido.id))
            pedido.status = STATUS_PREPARANDO
            pedido.save()
            return pedido, 200
        return None, 404


if __name__ == '__main__':
    app = FastAPI()
    @app.get('/restaurante/{nome}')
    def get_restaurante(nome: str):
        restaurante = Restaurante(nome=nome)
        return restaurante.recebe_pedidos()
    uvicorn.run(app)
