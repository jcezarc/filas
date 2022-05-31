from dataclasses import dataclass
from mongo_table import MongoTable
from pedido import Pedido, STATUS_PREPARANDO, STATUS_EM_TRANSPORTE
from fastapi import FastAPI
import uvicorn


@dataclass
class Entregador(MongoTable):
    nome: str

    def recebe_pedidos(self):
        busca = Pedido(restaurante=None, status=STATUS_PREPARANDO)
        encontrado = busca.find()
        if encontrado:
            primeiro = encontrado.pop(0)
            pedido = Pedido(**primeiro)
            print('{} entregando o pedido {}...'.format(
                self.nome,
                pedido.id
            ))
            pedido.status = STATUS_EM_TRANSPORTE
            pedido.entregador = self.nome
            pedido.save()
            return pedido, 200
        return None, 404


if __name__ == '__main__':
    app = FastAPI()
    @app.get('/entregador/{nome}')
    def get_entregador(nome: str):
        entregador = Entregador(nome=nome)
        return entregador.recebe_pedidos()
    uvicorn.run(app)
