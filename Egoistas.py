class Egoista:
    def __init__(self, mineradores_egoistas=[]):
        self.mineradores_egoistas = mineradores_egoistas

    def __str__(self):
        return 'Quantidade de mineradores egoístas: {}'.format(len(self.mineradores_egoistas))