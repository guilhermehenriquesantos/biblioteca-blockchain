from bloco import Bloco


class Blockchain:

    def __init__(self, minerador, bloco):
        self.minerador = minerador
        self.bloco = bloco

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
                blockchain = {}
                for propriedades in bloco:
                    detalhes = propriedades.strip().split(',')

                    numero_bloco = detalhes[0]
                    dados_bloco = detalhes[1]
                    hash_bloco_anterior = detalhes[2]
                    nonce = detalhes[3]
                    hash_deste_bloco = detalhes[4]

                    blockchain[numero_bloco] = Bloco(
                        numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco)

            return blockchain

        except Exception as error:
            print('\nAlgum erro ocorreu ao importar a blockchain\n', error)
