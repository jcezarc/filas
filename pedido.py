from uuid import uuid4
from mongo_table import MongoTable

STATUS_PENDENTE = 1
STATUS_PREPARANDO = 2
STATUS_EM_TRANSPORTE = 3
STATUS_ENTREGUE = 4


class Pedido(MongoTable):
    def __init__(self, restaurante: type, status: int, **args):
        self.id = str(uuid4())[:8]
        self.__restaurante = restaurante
        self.nome_restaurante = restaurante.nome
        self.pratos = {}
        self.status = status
        self.cliente = args.get('cliente', '')
        self.entregador = args.get('entregador', '')

    def add(self, prato: str, quantidade: int=1):
        self.pratos[prato] = quantidade

    def total(self) -> float:
        ref = self.__restaurante.pratos
        return sum(ref[p] * q for p, q in self.pratos.items())
