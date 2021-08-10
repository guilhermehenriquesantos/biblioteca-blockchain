from hashlib import sha256


MAX_NONCE = 100000000000


class Bloco:

    def __init__(self, numero, dados, hash_bloco_anterior=None, nonce=None, hash_deste_bloco=None):
        self.numero = numero
        self.dados = dados
        self.hash_bloco_anterior = hash_bloco_anterior
        self.nonce = nonce
        self.hash_deste_bloco = hash_deste_bloco

    def minerar_bloco(self, numero_bloco, transacoes_do_bloco, hash_anterior, quantidade_zeros_prefixo):
        prefixo_hash = '0'*quantidade_zeros_prefixo

        if (hash_anterior == None):
            hash_anterior = "0000000000000000000000000000000000000000000000000000000000000000"

        for nonce in range(MAX_NONCE):
            bloco = str(numero_bloco) + transacoes_do_bloco + \
                hash_anterior + str(nonce)
            hash_do_bloco = sha256(bloco.encode('ascii')).hexdigest()

            if hash_do_bloco.startswith(prefixo_hash):
                self.colocar_bloco_blockchain(
                    numero_bloco, transacoes_do_bloco, hash_anterior, nonce, hash_do_bloco)

        raise BaseException(
            '\nNão foi possível realizar a mineração. Foram feitas: {MAX_NONCE} de tentativas\n')
