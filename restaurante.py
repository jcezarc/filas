from mongo_table import MongoTable
from pedido import Pedido, STATUS_PENDENTE, STATUS_PREPARANDO


class Restaurante(MongoTable):
    def __init__(self, nome: str):
        self.nome = nome
        self.pratos = {}
        super().__init__()

    def add_prato(self, nome:str, preco:float):
        self.pratos[nome] = preco
        return self

    def recebe_pedidos(self):
        busca = Pedido(restaurante=self, status=STATUS_PENDENTE)
        encontrado = busca.find()
        if encontrado:
            dados = encontrado.pop(0)
            pedido = Pedido(self, **dados)
            msg = 'Preparando o pedido {}...'.format(pedido.id)
            pedido.status = STATUS_PREPARANDO
            pedido.save()
            return msg, 200
        return '', 404
