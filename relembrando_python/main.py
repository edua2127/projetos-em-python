from produto import Produto



def cadastro_produto():
    produto = Produto('Iphone', 3500.00, '2022-06-16')
    print('produto {} de valor {} foi cadastrado, data de entrega para {}'.format(produto.nome, produto.valor, produto.dataEntrega))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cadastro_produto()
