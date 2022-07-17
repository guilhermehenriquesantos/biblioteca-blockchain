import random
from array import array

from Bloco import Bloco
from Egoistas import Egoista
from Minerador import Minerador


class Mundo:
    def __init__(self, mineradores={}, poder_mundial=0, bifurcacoes={}, egoistas=None):
        self.mineradores = mineradores
        self.poder_mundial = poder_mundial
        self.bifurcacoes = bifurcacoes

        if (egoistas != None):
            self.egoistas = egoistas
        else:
            self.egoistas = Egoista()

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

    def ordenar_poder(self):
        self.mineradores = {key: value for key, value in sorted(
            self.mineradores.items(), key=lambda item: item[1])}

        return self

    def iniciar_processamento(self, quantidade_mineradores, quantidade_blocos_desejados):
        self.criar_mineradores(quantidade_mineradores)

        for minerador in self.mineradores.keys():
            while (len(minerador.blockchain.livro_razao) < quantidade_blocos_desejados):
                for minerador in self.mineradores.keys():
                    minerador.tentar_mineracao(self.poder_mundial)

                for minerador in self.mineradores.keys():
                    minerador.propagar_atualizacao(self.egoistas)

                self.detectar_bifurcacoes()

        return self

    def detectar_bifurcacoes(self):
        for minerador in self.mineradores.keys():
            for blockchain_comparativa in self.mineradores.keys():
                if ((len(minerador.blockchain.livro_razao) == len(blockchain_comparativa.blockchain.livro_razao)) and (minerador.blockchain.topo != blockchain_comparativa.blockchain.topo) and (minerador.blockchain.topo.hash_proprio == blockchain_comparativa.blockchain.topo.hash_proprio)):
                    self.bifurcacoes[len(
                        minerador.blockchain.livro_razao)] = {}
                    self.bifurcacoes[len(
                        minerador.blockchain.livro_razao)][minerador.blockchain.topo.hash_proprio] = {}

                    for hash, minerou_bloco in minerador.blockchain.historico_mineradores.items():
                        if (hash == minerador.blockchain.topo.hash_proprio):
                            self.bifurcacoes[len(minerador.blockchain.livro_razao)][minerador.blockchain.topo.hash_proprio][
                                minerou_bloco.identificador] = minerou_bloco.poder_computacional

                    for hash, minerou_bloco in blockchain_comparativa.blockchain.historico_mineradores.items():
                        if (hash == blockchain_comparativa.blockchain.topo.hash_proprio):
                            self.bifurcacoes[len(minerador.blockchain.livro_razao)][minerador.blockchain.topo.hash_proprio][
                                minerou_bloco.identificador] = minerou_bloco.poder_computacional

        return self
