from mongo_table import MongoTable
from buscador import Buscador
from pedido import Pedido, STATUS_PREPARANDO, STATUS_EM_TRANSPORTE


class Entregador(MongoTable, Buscador):
    def __init__(self, nome: str):
        self.nome = nome
        super().__init__()

    def busca_pedido(self) -> list:
        if not self.find():
            raise Exception('Entregador não cadastrado')
        return Pedido(status=STATUS_PREPARANDO).find()

    def atualiza(self, pedido) -> str:
        pedido.status = STATUS_EM_TRANSPORTE
        pedido.entregador = self.nome
        return '{} entregando o pedido {}...'.format(
            self.nome,
            pedido.id
        )
