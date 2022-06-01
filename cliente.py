from mongo_table import MongoTable
from buscador import Buscador
from pedido import Pedido, STATUS_EM_TRANSPORTE, STATUS_ENTREGUE


class Cliente(MongoTable, Buscador):
    def __init__(self, nome: str):
        self.nome = nome
        super().__init__()

    def busca_pedido(self) -> list:
        return Pedido(
            status=STATUS_EM_TRANSPORTE,
            cliente=self
        ).find()

    def atualiza(self, pedido) -> str:
        pedido.status = STATUS_ENTREGUE
        return 'Pedido {} recebido por {} !!'.format(
            pedido.id,
            self.nome
        )
