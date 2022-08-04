class Bloco:
    def __init__(self, minerador, numero=1, dados='Dados do bloco ', hash_anterior='0000000000000000000000000000000000000000000000000000000000000000', nonce=None, hash_proprio=None):
        self.minerador = minerador

        if(len(self.minerador.blockchain.livro_razao) > 0):
            self.numero = self.minerador.blockchain.topo.numero + 1
            self.hash_anterior = self.minerador.blockchain.topo.hash_proprio
        else:
            self.numero = numero
            self.hash_anterior = hash_anterior

        self.dados = dados + str(self.numero)
        self.nonce = nonce
        self.hash_proprio = hash_proprio

    def __str__(self):
        return 'Numero: {}\nDados: {}\nHash anterior: {}\nNonce: {}\nHash próprio: {}'.format(self.numero, self.dados, self.nonce, self.hash_anterior, self.hash_proprio)
