class Buscador:
    def busca_pedido(self) -> list:
        pass

    def atualiza(self, pedido) -> str:
        return ''

    def recebe_pedidos(self):
        encontrado = self.busca_pedido()
        if encontrado:
            dados = encontrado.pop(0)
            pedido = Pedido(**dados)
            msg = self.atualiza(pedido)
            pedido.save()
            return msg, 200
        return '', 404
