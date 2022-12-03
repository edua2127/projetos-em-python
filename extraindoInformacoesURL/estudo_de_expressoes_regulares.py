import re
rg = '11.000'

padrao = re.compile('[0-9]{2}[.]{0,1}[0-9]{3}')

busca = padrao.search(rg)

if busca:
    rg_encontrado = busca.group()
    print(rg_encontrado)