total_de_tentativas = 7
numero = 48
for rodada in range (1, total_de_tentativas + 1):
    print("tentativas:", rodada)
    chute = int(input("digite um numero entre 1 e 100: "))
    acertou = chute == numero
    maior = chute > numero
    if(chute < 0 or chute > 100) :
        print("digite um numero entre 1 e 100!!!")
        continue

    if(acertou) :
        print("voce acertou")
        break
    elif(maior):
        print("voce errou, digite um numero menor")
    else:
        print("voce errou, digite um numero maior")
print("fim do jogo")