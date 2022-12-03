url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


url = url.strip()

if url == "":
    raise ValueError("a URL está vazia")
# separa a URL base dos parametros
condicao_de_parada = url.find('?')
# URL BASE
url_base = url[:condicao_de_parada]

# SUBSTRING COM OS PARAMETROS = moedaOrigem=real&moedaDestino=dolar&quantidade=100
url_parametros = url[condicao_de_parada + 1:]

parametro_de_busca = 'quantidade'
# posicao inicial do parametro
posicao_inicial_parametro = url_parametros.find(parametro_de_busca)

# posicao_inical_do_valor
posicao_inicial_valor = posicao_inicial_parametro + len(parametro_de_busca) + 1

# posicao final do valor
# necessario verificar se é existe o ultimo parametro ou nao
posicao_e_comercial = url_parametros.find('&', posicao_inicial_valor)


if posicao_e_comercial == -1:
    valor = url_parametros[posicao_inicial_valor:]
else:
    valor = url_parametros[posicao_inicial_valor:posicao_e_comercial]

print(valor)
