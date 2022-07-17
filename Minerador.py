import random

from Blockchain import Blockchain
from Bloco import Bloco
from Mecanismo import Mecanismo


class Minerador:
    def __init__(self, identificador, mecanismo=None, poder_computacional=None, vizinhos=None, blockchain=None, propagar=False):
        self.identificador = identificador
        self.propagar = propagar

        if (mecanismo != None):
            self.mecanismo = mecanismo
        else:
            self.mecanismo = Mecanismo(self)

        if (poder_computacional != None):
            self.poder_computacional = poder_computacional
        else:
            self.poder_computacional = 0

        if (vizinhos != None):
            self.vizinhos = vizinhos
        else:
            self.vizinhos = []

        if (blockchain != None):
            self.blockchain = blockchain
        else:
            self.blockchain = Blockchain(self)

    def __str__(self):
        id = '1- Identificador: '
        consenso = '2- Mecanismo de consenso: PoW'
        poder = '3- Poder computacional: '
        quantidade_vizinhos = '4- Quantidade de vizinhos: '
        tamanho_blockchain = '5- Tamanho da blockchain: '

        return id + '{}\n'.format(self.identificador) + consenso + '\n' + poder + '{}\n'.format(self.poder_computacional) + quantidade_vizinhos + '{}\n'.format(len(self.vizinhos)) + tamanho_blockchain + '{}'.format(len(self.blockchain.livro_razao))

    def atualizar(self, blockchain_atualizada):
        try:
            self.blockchain.atualizar(blockchain_atualizada)
            self.propagar = True

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a atualização do minerador: {}'.format(error))
            return self

    def minerar(self, bloco, poder_mundial):
        try:
            self.mecanismo.bloco = bloco
            self.mecanismo.prova_de_trabalho()
            self.propagar = True
            self.mineracao_egoista(poder_mundial)

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a realização do processo de mineração: {}'.format(error))

    def propagar_atualizacao(self, mineradores_egoistas):
        egoista = False
        if (self.propagar):
            for i in range(len(self.vizinhos)):
                if (len(self.vizinhos[i].blockchain.livro_razao) < len(self.blockchain.livro_razao)):
                    if (len(self.blockchain.livro_razao) > (len(self.vizinhos[i].blockchain.livro_razao) + 1)):
                        for bloco, minerador in self.blockchain.historico_mineradores.items():
                            if (self.blockchain.topo.hash_proprio == bloco and self.identificador == minerador.identificador):
                                egoista = True
                    self.vizinhos[i].atualizar(self.blockchain)

            if (egoista):
                mineradores_egoistas.mineradores_egoistas.append(self)

            self.propagar = False

            return self

    def tentar_mineracao(self, poder_mundial):
        if ((random.uniform(0, 1)) <= (self.poder_computacional)/poder_mundial):
            bloco = self.criar_bloco()
            self.minerar(bloco, poder_mundial)
            return self

    def criar_bloco(self):
        if(self.blockchain.topo != None):
            numero_bloco = self.blockchain.topo.numero + 1
            dados = 'Dados do bloco ' + str(numero_bloco)
            bloco = Bloco(numero_bloco, dados,
                          self.blockchain.topo.hash_proprio)
            return bloco
        else:
            numero_bloco = 1
            dados = 'Dados do bloco ' + str(numero_bloco)
            bloco = Bloco(numero_bloco, dados)
            return bloco

    def mineracao_egoista(self, poder_mundial):
        for vizinho in self.vizinhos:
            if (vizinho.propagar == True or vizinho.poder_computacional > self.poder_computacional):
                return self

        self.tentar_mineracao(poder_mundial)
