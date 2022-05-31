from cliente import Cliente
from entregador import Entregador
from restaurante import Restaurante
from pedido import Pedido, STATUS_PENDENTE

DOCES = ['Arroz doce', 'Curau cremoso', 'Bananada de tacho']


def grava_pedido():
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
    for pessoa in list(params.values())[:3]:
        if not pessoa.find():
            print('Gravando {} "{}"...'.format(pessoa.__class__.__name__, pessoa.nome))
            pessoa.save()
    params.pop('entregador') # --- Só será atribuído quando retirar para transporte
    novo_pedido = Pedido(**params)
    for i in range(3):
        novo_pedido.add(DOCES[i], i+1)
    novo_pedido.save()
    return 'Valor do pedido {}: R$ {:.2f}'.format(
        novo_pedido.id, novo_pedido.total()
    ), 200

if __name__ == '__main__':
    print('-'*50)
    print( grava_pedido() )
