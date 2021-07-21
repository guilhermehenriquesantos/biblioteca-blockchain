import random


class Minerador:

    def __init__(self, identificador, poder_mineracao):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao

    def __str__(self):
        return "{} é um minerador com poder de mineração ({})".format(self.identificador, self.poder_mineracao)
    
