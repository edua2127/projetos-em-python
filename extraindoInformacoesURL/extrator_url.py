import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao.match(self.url)
        if not match:
            raise ValueError("URL INVALIDA")
        else:
            print('URL VALIDA')

    def get_url_base(self):
        condicao_de_parada = self.url.find('?')
        url_base = self.url[:condicao_de_parada]
        return url_base

    def get_url_parametros(self):
        condicao_de_parada = self.url.find('?')
        url_parametros = self.url[condicao_de_parada + 1:]
        return url_parametros

    def __len__(self):
        return self.url

    def __str__(self):
        return f'URL: {self.url} \nPARAMETROS DA URL: {self.get_url_parametros()} \nBASE DA URL: {self.get_url_base()}'
    def get_valor_parametros(self, parametro_de_busca):
        posicao_inicial_parametro = self.get_url_parametros().find(parametro_de_busca)
        posicao_inicial_valor = posicao_inicial_parametro + len(parametro_de_busca) + 1
        posicao_e_comercial = self.get_url_parametros().find('&', posicao_inicial_valor)
        if posicao_e_comercial == -1:
            valor = self.get_url_parametros()[posicao_inicial_valor:]
        else:
            valor = self.get_url_parametros()[posicao_inicial_valor:posicao_e_comercial]

        return valor


extrator = ExtratorURL("www.bytebank.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
                       )
print(extrator)
#valor = extrator.get_valor_parametros('moedaDestino')

#print(valor)
