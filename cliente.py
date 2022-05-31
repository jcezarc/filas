from dataclasses import dataclass
from mongo_table import MongoTable
from pedido import Pedido, STATUS_EM_TRANSPORTE, STATUS_ENTREGUE
from fastapi import FastAPI
import uvicorn



@dataclass
class Cliente(MongoTable):
    nome: str

    def recebe_pedidos(self):
        busca = Pedido(
            restaurante=None,
            status=STATUS_EM_TRANSPORTE,
            cliente=self.nome
        )
        encontrado = busca.find()
        if encontrado:
            primeiro = encontrado.pop(0)
            print('Pedido {} recebido por {} !!'.format(
                pedido.id,
                self.nome
            ))
            pedido = Pedido(**primeiro)
            pedido.status = STATUS_ENTREGUE
            pedido.save()
            return pedido, 200
        return None, 404


if __name__ == '__main__':
    app = FastAPI()
    @app.get('/cliente/{nome}')
    def get_cliente(nome: str):
        cliente = Cliente(nome=nome)
        return cliente.recebe_pedidos()
    uvicorn.run(app)
