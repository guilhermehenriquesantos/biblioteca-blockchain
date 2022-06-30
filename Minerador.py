from Blockchain import Blockchain
from Mecanismo import Mecanismo


class Minerador:
    def __init__(self, identificador, mecanismo=None, poder_computacional=None, vizinhos=None, blockchain=None):
        self.identificador = identificador

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
            self.propagar_atualizacao(self.blockchain)

            return self
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a atualização do minerador: {}'.format(error))
            return self

    def minerar(self, bloco):
        try:
            self.mecanismo.bloco = bloco
            self.mecanismo.prova_de_trabalho()
            self.propagar_atualizacao(self.blockchain)
        except Exception as error:
            print(
                'Ocorreu um erro que impossibilitou a realização do processo de mineração: {}'.format(error))

    def propagar_atualizacao(self, blockchain_atualizada):
        for i in range(len(self.vizinhos)):
            if (len(self.vizinhos[i].blockchain.livro_razao) < len(self.blockchain.livro_razao)):
                self.vizinhos[i].atualizar(blockchain_atualizada)
