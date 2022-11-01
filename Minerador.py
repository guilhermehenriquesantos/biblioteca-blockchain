import random

from Blockchain import Blockchain
from Bloco import Bloco
from Mecanismo import Mecanismo


class Minerador:
    def __init__(self, identificador, mecanismo=None, poder_computacional=None, vizinhos=None, blockchain=None, propagar=False, fraudador=False):
        self.identificador = identificador
        self.propagar = propagar
        self.fraudador = fraudador

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
        fraudador = '6- Frauda blocos: '

        return id + '{}\n'.format(self.identificador) + consenso + '\n' + poder + '{}\n'.format(self.poder_computacional) + quantidade_vizinhos + '{}\n'.format(len(self.vizinhos)) + tamanho_blockchain + '{}\n'.format(len(self.blockchain.livro_razao)) + fraudador + '{}'.format(str(self.fraudador))

    '''
    * Nome: atualizar
    * Parâmetros: próprio minerador e blockchain_atualizada (objeto Blockchain)
    * Objetivo: atualizar um minerador com a blockchain honesta mais atualizada do que a que ele possui e após essa atualização, informar a rede caso ele esteja apto a propagar essa nova blockchain, ou seja, caso não tenha recebido uma blockchain fraudada ele compartilha com a rede.
    *
    '''
    def atualizar(self, blockchain_atualizada):
        try:
            self.blockchain.atualizar(blockchain_atualizada)
            if (blockchain_atualizada.fraudada == True):
                self.propagar = False
            else:
                self.propagar = True

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a atualização do minerador: {}'.format(error))

    '''
    * Nome: minerar
    * Parâmetros: próprio minerador, bloco (bloco a ser inserido na blockchain)
    * Objetivo: informar ao mecanismo de consenso as informações necessárias para que ele possa executar o método de obtenção de consenso, neste caso a prova de trabalho. Após executar a prova de trabalho, o minerador possui um novo bloco e poderá propagar sua atualização pela rede.
    *
    '''
    def minerar(self, bloco):
        try:
            self.mecanismo.bloco = bloco
            self.mecanismo.prova_de_trabalho()
            self.propagar = True

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a realização do processo de mineração: {}'.format(error))

    '''
    * Nome: propagar_atualizacao
    * Parâmetros: próprio minerador
    * Objetivo: se um minerador estiver apto a propagar sua blockchain, ele irá percorrer os seus vizinhos e enviar essa atualização para cada um deles caso eles possuam uma blockchain menor do que a do minerador que está propagando.
    *
    '''
    def propagar_atualizacao(self):
        if (self.propagar):
            for i in range(len(self.vizinhos)):
                if (len(self.vizinhos[i].blockchain.livro_razao) < len(self.blockchain.livro_razao)):
                    self.vizinhos[i].atualizar(self.blockchain)

            self.propagar = False

            return self

    '''
    * Nome: tentar_mineracao
    * Parâmetros: próprio minerador e poder_mundial (poder computacional da rede)
    * Objetivo: realizar uma espécie de loteria para escolha de um minerador e nessa loteria, quanto maior o poder computacional de um minerador, maior a chance que ele terá de minerar um novo bloco. Se o minerador for do tipo fraudador ele irá minerar um bloco fraudado ao invés de um bloco honesto como os demais.
    *
    '''
    def tentar_mineracao(self, poder_mundial):
        if ((random.uniform(0, 1)) <= (self.poder_computacional)/poder_mundial):
            bloco = Bloco(self)

            if (self.fraudador == True):
                bloco.fraudado = True

            self.minerar(bloco)
            return self
