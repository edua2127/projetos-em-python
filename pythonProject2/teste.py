lista = []
for i in range(0, 4):
    lista.append(int(input("")))
produto1 = lista[0] * lista[1]
produto2 = lista[2] * lista[3]
diferenca = produto1 - produto2
print("DIFERENCA = {}".format(diferenca))