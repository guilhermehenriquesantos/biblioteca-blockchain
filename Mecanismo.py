from hashlib import sha256


class Mecanismo:
    def __init__(self, minerador, bloco=None):
        self.minerador = minerador
        self.bloco = bloco

    def __str__(self):
        if (self.bloco != None):
            return 'MINERADOR: {}\n\tINFORMAÇÕES DO BLOCO\n\t\tNumero: {}\n\t\tDados: {}'.format(self.minerador.identificador, self.bloco.numero, self.bloco.dados)
        else:
            return 'MINERADOR: {}'.format(self.minerador.identificador)

    def prova_de_trabalho(self):
        quantidade_prefixo = 4
        prefixo = '0'*quantidade_prefixo
        maximo_nonce = 100000000000
        bloco_genesis = '0000000000000000000000000000000000000000000000000000000000000000'

        if (len(self.minerador.blockchain.livro_razao) > 0):
            self.bloco.hash_anterior = self.minerador.blockchain.topo.hash_proprio
        else:
            self.bloco.hash_anterior = bloco_genesis

        for nonce in range(maximo_nonce):
            informacoes_bloco = str(self.bloco.numero) + \
                self.bloco.dados + \
                self.bloco.hash_anterior + \
                str(nonce)

            hash_bloco = sha256(informacoes_bloco.encode('ascii')).hexdigest()

            if hash_bloco.startswith(prefixo):
                self.bloco.nonce = nonce
                self.bloco.hash_proprio = hash_bloco

                self.minerador.blockchain.inserir(self.bloco)

                return self.minerador

        raise BaseException(
            '\nNão foi possível realizar a mineração. Foram feitas: {valor_maximo_nonce} de tentativas\n')
