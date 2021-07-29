from hashlib import sha256


MAX_NONCE = 100000000000


class Bloco:

    def __init__(self, numero, dados, hash_bloco_anterior=None, nonce=None, hash_deste_bloco=None):
        self.numero = numero
        self.dados = dados
        self.hash_bloco_anterior = hash_bloco_anterior
        self.nonce = nonce
        self.hash_deste_bloco = hash_deste_bloco

    def colocar_bloco_blockchain(self, numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco):
        blockchain = {}
        blockchain[numero_bloco] = Bloco(
            numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco)

        return blockchain

    # Ter um método para criar o bloco e outro para colocar na blockchain

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

    def exportar_blockchain(self, bloco):
        try:
            with open('blockchain.csv', 'w') as blockchain_arquivo:
                numero_bloco = bloco.numero
                dados_bloco = bloco.dados
                hash_bloco_anterior = bloco.hash_bloco_anterior
                nonce = bloco.nonce
                hash_deste_bloco = bloco.hash_deste_bloco

                blockchain_arquivo.write('{},{},{},{},{}\n'.format(
                    numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)

    def importar_blockchain(self):
        try:
            with open('blockchain.csv', 'r') as blockchain_arquivo:
                bloco = blockchain_arquivo.readlines()
                for propriedades in bloco:
                    detalhes = propriedades.strip().split(',')

                    numero_bloco = detalhes[0]
                    dados_bloco = detalhes[1]
                    hash_bloco_anterior = detalhes[2]
                    nonce = detalhes[3]
                    hash_deste_bloco = detalhes[4]

                    self.colocar_bloco_blockchain(numero_bloco, dados_bloco,
                                                  hash_bloco_anterior, nonce, hash_deste_bloco)

        except Exception as error:
            print('\nAlgum erro ocorreu ao importar a blockchain\n', error)
