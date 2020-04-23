class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Beijo no rosto'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    fulano = Mutante(nome='fulano')
    lorena = Mulher(fulano, nome='Lorena')
    print(Pessoa.cumprimentar(lorena))
    print(id(lorena))
    print(lorena.cumprimentar())
    print(lorena.nome)
    print(lorena.idade)
    for filho in lorena.filhos:
        print(filho.nome)
    lorena.sobrenome = 'Ribeiro'
    del lorena.filhos
    lorena.olhos = 1
    del lorena.olhos
    print(lorena.__dict__)
    print(fulano.__dict__)
    print(lorena.olhos)
    print(fulano.olhos)
    print(id(Pessoa.olhos), id(lorena.olhos), id(fulano.olhos))
    print(Pessoa.metodo_estatico(), lorena.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), lorena.nome_e_atributos_de_classe())
    pessoa = Pessoa('anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(isinstance(lorena, Pessoa))
    print(isinstance(lorena, Pessoa))
    print(fulano.olhos)
    print(lorena.cumprimentar())
    print(fulano.cumprimentar())