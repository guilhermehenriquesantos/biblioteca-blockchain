from blockchain import Blockchain, Bloco
import random


class Minerador:

    def __init__(self, identificador, poder_mineracao):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao

    # Esse parâmetro deveria ser uma classe do tipo bloco
    def minerando_bloco():
        pass


class MineradorPoderoso(Minerador):

    def __init__(self, identificador, poder_mineracao=random.randint(61, 100), tipo_minerador="Poderoso"):
        super().__init__(identificador=identificador, poder_mineracao=poder_mineracao)
        self.tipo_minerador = tipo_minerador

    def __str__(self):
        return "{} é um minerador do tipo {} com poder de mineração de {}".format(self.identificador, self.tipo_minerador, self.poder_mineracao)


class MineradorMediano(Minerador):

    def __init__(self, identificador, poder_mineracao=random.randint(21, 60), tipo_minerador="Mediano"):
        super().__init__(identificador=identificador, poder_mineracao=poder_mineracao)
        self.tipo_minerador = tipo_minerador

    def __str__(self):
        return "{} é um minerador do tipo {} com poder de mineração de {}".format(self.identificador, self.tipo_minerador, self.poder_mineracao)


class MineradorFraco(Minerador):

    def __init__(self, identificador, poder_mineracao=random.randint(1, 20), tipo_minerador="Fraco"):
        super().__init__(identificador=identificador, poder_mineracao=poder_mineracao)
        self.tipo_minerador = tipo_minerador

    def __str__(self):
        return "{} é um minerador do tipo {} com poder de mineração de {}".format(self.identificador, self.tipo_minerador, self.poder_mineracao)


class MineradorAleatorio(Minerador):

    def __init__(self, identificador, poder_mineracao=random.randint(1, 100), tipo_minerador=None):
        super().__init__(identificador=identificador, poder_mineracao=poder_mineracao)

        if (poder_mineracao <= 20):
            tipo_minerador = "Aleatorio Fraco"
            self.tipo_minerador = tipo_minerador
        elif (poder_mineracao > 20 and poder_mineracao <= 60):
            tipo_minerador = "Aleatorio Mediano"
            self.tipo_minerador = tipo_minerador
        elif (poder_mineracao > 60 and poder_mineracao <= 100):
            tipo_minerador = "Aleatorio Forte"
            self.tipo_minerador = tipo_minerador

    def __str__(self):
        return "{} é um minerador do tipo {} com poder de mineração de {}".format(self.identificador, self.tipo_minerador, self.poder_mineracao)
