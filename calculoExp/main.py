anos = 1000
taxa_crescimento=1000
valor_inicial=100
periodo_de_ciclo=10

numero_de_ciclos = anos/periodo_de_ciclo
numero_de_ciclos = int(numero_de_ciclos)

for indice in range(numero_de_ciclos):
    valor_inicial = valor_inicial * taxa_crescimento
    print('{:e}'.format(valor_inicial))


