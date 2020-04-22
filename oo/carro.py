"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado velocidade:
2) Método acelerar, que deverá incrementar a velocidade de uma unidade.
3) Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

   N
O     L
   S

     Exemplo:
     >>> # Testando motor
     >>> motor = Motor()
     >>> motor.velocidade
     0
     >>> motor.acelerar()
     >>> motor.velocidade
     1
     >>> motor.acelerar()
     >>> motor.velocidade
     2
     >>> motor.acelerar()
     >>> motor.velocidade
     3
     >>> motor.frear()
     >>> motor.velocidade
     1
     >>> motor.frear()
     >>> motor.velocidade
     0
     >>> # Testando Direção
     >>> direção = Direção()
     >>> direção.valor
     'Norte'
     >>> direção.girar_a_direita()
     >>> direção.valor
     'Leste'
     >>> direção.girar_a_direita()
     >>> direção.valor
     'Sul'
     >>> direção.girar_a_direita()
     >>> direção.valor
     'Oeste'
     >>> direção.girar_a_direita()
     >>> direção.valor
     'Norte'
     >>> direção.girar_a_esquerda()
     >>> direção.valor
     'Oeste'
     >>> direção.girar_a_esquerda()
     >>> direção.valor
     'Sul'
     >>> direção.girar_a_esquerda()
     >>> direção.valor
     'Leste'
     >>> direção.girar_a_esquerda()
     >>> direção.valor
     'Norte'
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     1
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     2
     >>> carro.frear()
     >>> carro.calcular_velocidade()
     0
     >>> carro.calcular_a_direção()
     'Norte'
     >>> carro.girar_a_direita()
     >>> carro.calcular_a_direção()
     'Leste'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_a_direção()
     'Norte'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_a_direção()
     'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direção:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

