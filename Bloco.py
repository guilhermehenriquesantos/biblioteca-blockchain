class Bloco:
    def __init__(self, numero=None, dados=None, hash_anterior=None, nonce=None, hash_proprio=None):
        self.numero = numero
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.nonce = nonce
        self.hash_proprio = hash_proprio

    def __str__(self):
        return 'Numero: {}\nDados: {}\nHash anterior: {}\nNonce: {}\nHash próprio: {}'.format(self.numero, self.dados, self.nonce, self.hash_anterior, self.hash_proprio)

    '''
    * Nome: criar_bloco
    * Parâmetros: próprio bloco e minerador
    * Objetivo: criar um bloco de acordo com os dados de um minerador, se ele já possui uma blockchain, criar um bloco a partir dos dados já existentes nela, se ele não possui blockchain, significa que é o bloco gênesis sendo criado.
    *
    '''
    def criar_bloco(self, minerador):
        if(minerador.blockchain.topo != None):
            self.numero = minerador.blockchain.topo.numero + 1
            self.dados = 'Dados do bloco ' + str(self.numero)
            self.hash_anterior = minerador.blockchain.topo.hash_proprio

            return self
        else:
            self.numero = 1
            self.dados = 'Dados do bloco ' + str(self.numero)

            return self
