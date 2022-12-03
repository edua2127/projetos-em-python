class PessoaFisica:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def printe(self):
        return f'meu nome é {self.nome} e meu saldo é {self.saldo}'



class PessoaJuridica:
    def __init__(self, nome_empresa, cnpj, endereco):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.endereco = endereco

    def dados(self):
        return f'apresentacao da empresa: {self.nome_empresa}, CNPJ: {self.cnpj}, Endereço: {self.endereco}'
class Cliente(PessoaFisica, PessoaJuridica):
    pass

clienteNovo = Cliente('eduardo', 5000)
clienteNovo.nome_empresa = 'ESM'
clienteNovo.cnpj = 55555
clienteNovo.endereco = 'vila c'


print(clienteNovo.dados())