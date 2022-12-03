import console as console


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    def __str__(self):
        return f'\nnome da serie {self.nome}\nano da serie: {self.ano}\nnumero de temporadas: {self.duracao}\n'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, nova_temporada):
        self._temporadas = nova_temporada

    def __str__(self):
        return f'\nnome do filme: {self.nome}\nano do filme: {self.ano}\nduracao do filme: {self.temporadas}\n'


class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def programas(self):
        return self._programas

    @programas.setter
    def programas(self, novo_programa):
        self._programas = novo_programa

    def __len__(self):
        return len(self._programas)

lista = [Filme('vingadores', 2001, 150), Filme('Doutor estranho', 2015, 160)]
playlist = Playlist('playList de filmes', lista)

for programas in playlist:
    print(programas)




