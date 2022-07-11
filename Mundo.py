from array import array
import random
from Bloco import Bloco
from Minerador import Minerador


class Mundo:
    def __init__(self, mineradores={}, poder_mundial=0):
        self.mineradores = mineradores
        self.poder_mundial = poder_mundial

    def criar_mineradores(self, quantidade_mineradores):
        for identificador in range(1, quantidade_mineradores + 1):
            novo_minerador = Minerador(
                identificador, None, random.randint(1, 100))

            self.mineradores[novo_minerador] = novo_minerador.poder_computacional

        self.descobrir_poder_mundial()
        self.definir_vizinhos_minerador()
        return self

    def descobrir_poder_mundial(self):
        for poder in self.mineradores.values():
            self.poder_mundial = self.poder_mundial + poder

        return self

    def definir_vizinhos_minerador(self):
        for minerador in self.mineradores.keys():
            quantidade_vizinhos = random.randint(1, len(self.mineradores) - 1)

            for i in range(0, quantidade_vizinhos):
                vizinho_escolhido = random.choice(
                    list(self.mineradores.keys()))
                while(vizinho_escolhido.identificador == minerador.identificador and vizinho_escolhido in minerador.vizinhos):
                    vizinho_escolhido = random.choice(
                        list(self.mineradores.keys()))

                minerador.vizinhos.append(vizinho_escolhido)

        return self

    def sortear_minerador(self, dificuldade_sorteio):
        loteria = random.randint(1, dificuldade_sorteio*self.poder_mundial)
        acumulado = 0

        for minerador in self.mineradores.keys():
            acumulado = acumulado + minerador.poder_computacional
            if (loteria < acumulado):
                bloco = self.criar_bloco(minerador)
                minerador.minerar(bloco)
                return self

        return None

    def ordenar_poder(self):
        self.mineradores = {key: value for key, value in sorted(
            self.mineradores.items(), key=lambda item: item[1])}

        return self

    def criar_bloco(self, minerador):
        if(minerador.blockchain.topo != None):
            numero_bloco = minerador.blockchain.topo.numero + 1
            dados = 'Dados do bloco ' + str(numero_bloco)
            bloco = Bloco(numero_bloco, dados,
                          minerador.blockchain.topo.hash_proprio)
            return bloco
        else:
            numero_bloco = 1
            dados = 'Dados do bloco ' + str(numero_bloco)
            bloco = Bloco(numero_bloco, dados)
            return bloco
