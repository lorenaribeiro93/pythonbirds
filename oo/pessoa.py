class Pessoa:
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pérola = Pessoa(nome='Pérola')
    lorena = Pessoa(pérola, nome='Lorena')
    print(Pessoa.cumprimentar(lorena))
    print(id(lorena))
    print(lorena.cumprimentar())
    print(lorena.nome)
    print(lorena.idade)
    for filho in lorena.filhos:
        print(filho.nome)
    lorena.sobrenome = 'Ribeiro'
    del lorena.filhos
    print(lorena.__dict__)
    print(pérola.__dict__)
