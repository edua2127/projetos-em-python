
def exercicio1():
    vetor_numeros = []

    for i in range(0, 4):
        vetor_numeros.append(int(input("digite um numero: ")))

    print(vetor_numeros)


def exercicio2():
    lista = []
    for i in range(0, 4):
        lista.append(int(input("")))

    produto1 = lista[0] * lista[1]
    produto2 = lista[2] * lista[3]

    diferenca = produto1 - produto2

    print("DIFERENCA = {}".format(diferenca))


def exercicio3():
    nome = input()
    salario = float(input())
    total_vendas = float(input())

    total_receber = salario + (total_vendas * 0.15)
    print("TOTAL = R$ {:.2f}".format(total_receber))


def exercicio4():
    segundos = int(input())
    minutos = 0
    horas = 0
    if segundos >= 60:
        while segundos >= 60:
            minutos += 1
            segundos -= 60
            if minutos >= 60:
                minutos -= 60
                horas += 1
    print("{}:{}:{}".format(horas, minutos, segundos))


if __name__ == '__main__':
    exercicio4()
