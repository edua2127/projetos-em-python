import random

total = 7
numero_aleatorio = random.randrange(1, 101)
print("*OBS: DIGITE UM NUMERO DE 1 A 100!")
for rodada in range(1, total + 1):
    print("---------------------------------")
    chute = int(input("digite o seu chute: "))

    acertou = chute == numero_aleatorio
    maior = chute > numero_aleatorio
    menor = chute < numero_aleatorio

    if(chute > 100 or chute < 0):
        print("voce digitou um numero nao permitido!!!, escreve um numero de 1 a 100!!!")
        continue
    if(acertou):
        print("voce acertou, parabens")
        break
    elif(maior):
        print("voce errou, digite um numero menor")
    else:
        print("voce errou, digite um numero maior")


print("o numero aleatorio era: {}".format(numero_aleatorio))