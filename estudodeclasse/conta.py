class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("numero: {}\ntitular: {}\nsaldo: {}\nlimite: {}"
              .format(self.__numero, self.__titular, self.__saldo, self.__limite))

    def deposita(self, deposito):
        self.__saldo += deposito

    def __pode_sacar(self, valor_sacado):
        valor_disponivel = self.__saldo + self.__limite
        return valor_sacado <= valor_disponivel

    def saque(self, valor_sacado):
        if(self.__pode_sacar(valor_sacado)):
            self.__saldo -= valor_sacado
        else:
            print(" o valor {} não é possivel de ser sacado".format(valor_sacado))

    def transfere(self, valor, destino):
        if(self.__pode_sacar(valor)):
            self.saque(valor)
            destino.deposita(valor)
        else:
            print("o valor {} não é possivel de ser transferido".format(valor))
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
