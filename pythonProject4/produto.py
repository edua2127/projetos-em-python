class Produto:
    peso_maximo = 10
    def __init__(self, nome, descricao, peso_item):
        self._nome = nome
        self._descricao = descricao
        self._peso_item = peso_item
        self.peso_valido()

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def peso_valido(self):
        if self._peso_item > self.peso_maximo:
            raise Exception


roupa = Produto('adidas', 'vermelha', 5)
print(roupa.nome)
