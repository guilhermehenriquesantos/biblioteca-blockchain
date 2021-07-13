import random


class Minerador:

    def __init__(self, identificador, poder_mineracao, tipo_minerador=None):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        
        if (poder_mineracao <= 20):
            tipo_minerador = "Fraco"
            self.tipo_minerador = tipo_minerador
        elif (poder_mineracao > 20 and poder_mineracao <= 60):
            tipo_minerador = "Mediano"
            self.tipo_minerador = tipo_minerador
        elif (poder_mineracao > 60 and poder_mineracao <= 100):
            tipo_minerador = "Forte"
            self.tipo_minerador = tipo_minerador

    def __str__(self):
        return "{} é um minerador do tipo {} com poder de mineração de {}".format(self.identificador, self.tipo_minerador, self.poder_mineracao)
    
