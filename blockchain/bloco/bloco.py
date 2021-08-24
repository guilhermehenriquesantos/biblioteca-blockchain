class Bloco:

    def __init__(self, numero, dados, hash_bloco_anterior=None, nonce=None, hash_deste_bloco=None):
        self.numero = numero
        self.dados = dados
        self.hash_bloco_anterior = hash_bloco_anterior
        self.nonce = nonce
        self.hash_deste_bloco = hash_deste_bloco
