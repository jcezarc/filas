"""
Cria pedidos fictícios para testar o sistema.
Cada tipo de usuário (Restaurante, Cliente, MotoBoy)
... pode rodar o app separadamente e consumir a fila
"""

from cliente import Cliente
from entregador import Entregador
from restaurante import Restaurante
from pedido import Pedido, STATUS_PENDENTE

DOCES = ['Arroz doce', 'Curau cremoso', 'Bananada de tacho']


if __name__ == '__main__':
    params = {
        'cliente': Cliente('Sheila Kely Maria Creuza'),
        'entregador': Entregador('Lucia Santoro Gusmão'),
        'restaurante': Restaurante('Doces da vovó Regina'),
        'status': STATUS_PENDENTE
    }
    params['restaurante'].add_prato(
        DOCES[0], 8.90
    ).add_prato(
        DOCES[1], 7.15
    ).add_prato(
        DOCES[2], 11.10
    )
    for pessoa in params.values():
        if not pessoa.find():
            pessoa.save()
    novo_pedido = Pedido(**params)
    for i in range(3):
        novo_pedido.add(DOCES[i], i+1)
    novo_pedido.save()
    print('Valor do pedido {}: R$ {:.2f}'.format(
        novo_pedido.id, novo_pedido.total()
    )) # valor esperado: 56.5
