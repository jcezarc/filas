from mongo_table import MongoTable
from pedido import Pedido, STATUS_PREPARANDO, STATUS_EM_TRANSPORTE


class Entregador(MongoTable):
    def __init__(self, nome: str):
        self.nome = nome
        super().__init__()

    def recebe_pedidos(self):
        busca = Pedido(status=STATUS_PREPARANDO)
        encontrado = busca.find()
        if encontrado:
            dados = encontrado.pop(0)
            pedido = Pedido(**dados)
            msg = '{} entregando o pedido {}...'.format(
                self.nome,
                pedido.id
            )
            pedido.status = STATUS_EM_TRANSPORTE
            pedido.entregador = self.nome
            pedido.save()
            return msg, 200
        return '', 404
