class Minerador:

    def __init__(self, identificador, poder_mineracao, blocos_minerados=0):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        self.blocos_minerados = blocos_minerados

    def __str__(self):
        return "{} é um minerador com poder de mineração ({}) | Já minerou {} blocos".format(self.identificador, self.poder_mineracao, self.blocos_minerados)

    def exportar_minerador(self, minerador):
        try:
            with open('mineradores.csv', 'w') as mineradores:
                identificador = minerador.identificador
                poder_mineracao = minerador.poder_mineracao
                blocos_minerados = minerador.blocos_minerados

                mineradores.write('{},{},{}\n'.format(
                    identificador, poder_mineracao, blocos_minerados))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)

    def importar_mineradores(self):
        try:
            with open('mineradores.csv', 'r') as mineradores:
                minerador = mineradores.readlines()
                mineradores = {}
                for propriedades in minerador:
                    detalhes = propriedades.strip().split(',')

                    identificador = detalhes[0]
                    poder_mineracao = detalhes[1]
                    blocos_minerados = detalhes[2]

                    mineradores[poder_mineracao] = Minerador(
                        identificador, poder_mineracao, blocos_minerados)

            return mineradores

        except Exception as error:
            print('\nAlgum erro ocorreu ao importar os mineradores\n', error)
