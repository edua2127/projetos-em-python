import random


def jogo_forca():
    apresentacao()

    palavra_secreta = leitura_de_arquivo()
    lista_de_acertos = inicializa_lista_de_acertos(palavra_secreta)
    enforcou = False
    acertou = False
    # variaveis de verificacao
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()
        if chute.upper() in palavra_secreta.upper():
            lista_de_acertos = marca_chute_acertados(chute, palavra_secreta, lista_de_acertos)
        else:
            erros += 1
            print("tentativas restantes: {}".format(len(palavra_secreta) - erros))
            desenha_forca(erros)
        print(lista_de_acertos)
        if erros == 7:
            print_mensagem_perdedor(palavra_secreta)
            break
        if "_" not in lista_de_acertos:
            print_mensagem_vencedor()
            break


def marca_chute_acertados(chute, palavra_secreta, lista_de_acertos):
    index = 0
    for letra in palavra_secreta:
        if letra.upper() == chute.upper():
            lista_de_acertos[index] = letra
        index += 1
    return lista_de_acertos


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")


def apresentacao():
    print("=====================")
    print("=== JOGO DA FORCA ===")
    print("=====================")


def leitura_de_arquivo(nome_arquivo="palavras.txt"):
    arquivo = open("C:\\Users\\magal\\PycharmProjects\\jogos\\{}".format(nome_arquivo), "r")
    lista = []
    for linha in arquivo:
        linha = linha.strip().upper()
        lista.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(lista))
    return lista[numero]


def inicializa_lista_de_acertos(palavra_scecreta):
    return ["_" for _ in palavra_scecreta]


def pede_chute():
    return input("Qual o seu chute ? ").strip().upper()


if __name__ == "__main__":
    jogo_forca()
