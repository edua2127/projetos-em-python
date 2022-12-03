# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cliente import Cliente
from conta import ContaCorrente


def print_hi():
    cliente = Cliente('eduardo')
    print("nome atual: {}".format(cliente.nome))

    cliente.nome = input("digite o novo nome: ")
    print("--------------")
    print("novo nome: {}".format(cliente.nome))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
