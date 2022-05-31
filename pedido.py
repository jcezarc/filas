from uuid import uuid4
from mongo_table import MongoTable

STATUS_PENDENTE = 1
STATUS_PREPARANDO = 2
STATUS_EM_TRANSPORTE = 3
STATUS_ENTREGUE = 4


class Pedido(MongoTable):
    def __init__(self, restaurante: type, **args):
        def extrai_nome(key: str):
            obj = args.get(key, '')
            if hasattr(obj, 'nome'):
                return obj.nome
            return obj
        self.id = args.get('id')
        self.__restaurante = restaurante
        if restaurante:
            self.nome_restaurante = restaurante.nome
        self.pratos = {}
        self.status = args.get('status', 0)
        self.cliente = extrai_nome('cliente')
        self.entregador = extrai_nome('entregador')
        super().__init__()

    def add(self, prato: str, quantidade: int=1):
        if not self.id:
            self.id = str(uuid4())[:8]
        self.pratos[prato] = quantidade

    def total(self) -> float:
        ref = self.__restaurante.pratos
        return sum(ref[p] * q for p, q in self.pratos.items())
