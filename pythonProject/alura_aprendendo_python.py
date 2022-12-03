print("jogo de adivinhacao")

n_secreto = 48
total = 6
rodada = 1
while(rodada <= total):
    print("tentativa {} de {}".format(rodada, total))
    chute = int(input("digite um numero: "))

    acertou = chute == n_secreto
    maior = chute > n_secreto
    menor = chute < n_secreto

    if(acertou):
        print("voce acertou")
        rodada = 5
    elif(maior):
        print("voce errou, digite um numero mais baixo")
    elif(menor):
        print("voce errou, digite um numero maior")
    rodada = rodada + 1
