from uuid import uuid4
from mongo_table import MongoTable

STATUS_PENDENTE = 1
STATUS_PREPARANDO = 2
STATUS_EM_TRANSPORTE = 3
STATUS_ENTREGUE = 4


class Pedido(MongoTable):
    def __init__(self, **args):
        self._precos = {}
        def extrai_nome(key: str):
            obj = args.get(key, '')
            if hasattr(obj, 'nome'):
                if key == 'restaurante':
                    self._precos = obj.pratos
                return obj.nome
            return obj
        self.id = args.get('id')
        self.pratos = {}
        self.status = args.get('status', 0)
        self.cliente = extrai_nome('cliente')
        self.entregador = extrai_nome('entregador')
        self.restaurante = extrai_nome('restaurante')
        super().__init__()

    def add(self, prato: str, quantidade: int=1):
        if not self.id:
            self.id = str(uuid4())[:8]
        self.pratos[prato] = quantidade

    def total(self) -> float:
        ref = self._precos
        return sum(ref[p] * q for p, q in self.pratos.items())
