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

    '''
    * Nome: atualizar
    * Parâmetros: próprio minerador e blockchain_atualizada (objeto Blockchain)
    * Objetivo: atualizar um minerador com uma blockchain mais atualizada do que a que ele possui e após essa atualização, informar a rede que ele está apto a propagar essa nova blockchain.
    *
    '''
    def atualizar(self, blockchain_atualizada):
        try:
            self.blockchain.atualizar(blockchain_atualizada)
            self.propagar = True

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a atualização do minerador: {}'.format(error))

    '''
    * Nome: minerar
    * Parâmetros: próprio minerador, bloco (bloco a ser inserido na blockchain) e poder_mundial (poder computacional da rede)
    * Objetivo: informar ao mecanismo de consenso as informações necessárias para que ele possa executar o método de obtenção de consenso, neste caso a prova de trabalho. Após executar a prova de trabalho, o minerador possui um novo bloco e poderá propagar sua atualização pela rede. Ele também chamará o método de verificação de aptidão para poder realizar o processo de mineração egoísta.
    *
    '''
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

    '''
    * Nome: propagar_atualizacao
    * Parâmetros: próprio minerador e mineradores_egoistas (objeto que contém todos os mineradores que realizaram o processo de mineração egoísta)
    * Objetivo: se um minerador estiver apto a propagar sua blockchain, ele irá percorrer os seus vizinhos e enviar essa atualização para cada um deles caso eles possuam uma blockchain menor do que a do minerador que está propagando. Caso o minerador tenha uma blockchain com dois ou mais blocos a repassar para algum vizinho, significa que ele realizou o processo de mineração egoísta, então essa informação é repassada ao objeto que contém os mineradores egoístas.
    *
    '''
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

    '''
    * Nome: tentar_mineracao
    * Parâmetros: próprio minerador e poder_mundial (poder computacional da rede)
    * Objetivo: realizar uma espécie de loteria para escolha de um minerador e nessa loteria, quanto maior o poder computacional de um minerador, maior a chance que ele terá de minerar um novo bloco.
    *
    '''
    def tentar_mineracao(self, poder_mundial):
        if ((random.uniform(0, 1)) <= (self.poder_computacional)/poder_mundial):
            bloco = Bloco()
            bloco.criar_bloco(self)
            self.minerar(bloco, poder_mundial)
            return self

    '''
    * Nome: mineracao_egoista
    * Parâmetros: próprio minerador e poder_mundial (poder computacional da rede)
    * Objetivo: verificar se um minerador tem a capacidade de tentar realizar o processo de mineração egoísta.
    *
    '''
    def mineracao_egoista(self, poder_mundial):
        for vizinho in self.vizinhos:
            if (vizinho.propagar == True or vizinho.poder_computacional > self.poder_computacional):
                return self

        self.tentar_mineracao(poder_mundial)
