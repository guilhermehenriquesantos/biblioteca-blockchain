class Minerador:

    def __init__(self, identificador, poder_mineracao, blocos_minerados=0):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        self.blocos_minerados = blocos_minerados

    def __str__(self):
        return '{} é um minerador com poder de mineração ({}) | Já minerou {} blocos'.format(self.identificador, self.poder_mineracao, self.blocos_minerados)
