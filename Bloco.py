class Bloco:
    def __init__(self, numero, dados, hash_anterior=None, nonce=None, hash_proprio=None):
        self.numero = numero
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.nonce = nonce
        self.hash_proprio = hash_proprio

    def __str__(self):
        return 'Numero: {}\nDados: {}\nHash anterior: {}\nNonce: {}\nHash próprio: {}'.format(self.numero, self.dados, self.nonce, self.hash_anterior, self.hash_proprio)
