# caminho C:\Users\magal\PycharmProjects\jogos
import forca
import adivinhacao
def escolha_seu_jogo():
    print("================================")
    print("===bem vindo ao menu de jogos===")
    print("================================")

    print("\nescolha o jogo de usa preferencia")

    print("\n(1) forca")
    print("\n\n(2) adivinhação")

    jogo = int(input("\n\nopcao: "))

    if (jogo == 1):
        print("jogo da forca selecionado")
        forca.jogo_forca()
    elif (jogo == 2):
        print("jogo da adivinhação selecionado")
        adivinhacao.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolha_seu_jogo()