from mongo_table import MongoTable
from buscador import Buscador
from pedido import Pedido, STATUS_PENDENTE, STATUS_PREPARANDO


class Restaurante(MongoTable, Buscador):
    def __init__(self, nome: str):
        self.nome = nome
        self.pratos = {}
        super().__init__()

    def busca_pedido(self) -> list:
        return Pedido(
            restaurante=self,
            status=STATUS_PENDENTE
        ).find()

    def atualiza(self, pedido) -> str:
        pedido.status = STATUS_PREPARANDO
        return 'Preparando o pedido {}...'.format(pedido.id)

    def add_prato(self, nome:str, preco:float):
        self.pratos[nome] = preco
        return self
