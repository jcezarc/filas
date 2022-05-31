from mongo_table import MongoTable
from restaurante import Restaurante
from pedido import Pedido, STATUS_EM_TRANSPORTE, STATUS_ENTREGUE


class Cliente(MongoTable):
    def __init__(self, nome: str):
        self.nome = nome
        super().__init__()

    def recebe_pedidos(self):
        busca = Pedido(
            restaurante=None,
            status=STATUS_EM_TRANSPORTE,
            cliente=self.nome
        )
        encontrado = busca.find()
        if encontrado:
            dados = encontrado.pop(0)
            pedido = Pedido(Restaurante(
                dados['nome_restaurante']),
                **dados
            )
            msg = 'Pedido {} recebido por {} !!'.format(
                pedido.id,
                self.nome
            )
            pedido.status = STATUS_ENTREGUE
            pedido.save()
            return msg, 200
        return '', 404
