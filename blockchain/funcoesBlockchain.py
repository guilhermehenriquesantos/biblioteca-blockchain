from blockchain.bloco.bloco import Bloco

BLOCKCHAIN = {}


def incluir_bloco(bloco):
    BLOCKCHAIN[bloco.numero] = bloco


def exibir_blockchain(blockchain):
    if (len(blockchain) == 0):
        print(
            '>>>> Ainda não temos uma blockchain criada, crie ou importe a sua blockchain')
    else:
        for bloco in blockchain.keys():
            print('>>>> Bloco: {}\t Dados: {}\t Hash do bloco anterior:{}\t Nonce: {}\t Hash deste bloco {}'.format(
                bloco.numero, bloco.dados, bloco.hash_bloco_anterior, bloco.nonce, bloco.hash_deste_bloco))


def exportar_blockchain():
    try:
        with open('blockchain.csv', 'w') as blockchain_arquivo:
            for bloco in BLOCKCHAIN.values():
                numero_bloco = bloco.numero
                dados_bloco = bloco.dados
                hash_bloco_anterior = bloco.hash_bloco_anterior
                nonce = bloco.nonce
                hash_deste_bloco = bloco.hash_deste_bloco

                blockchain_arquivo.write('{},{},{},{},{}\n'.format(
                    numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco))

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)


def importar_blockchain():
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

                bloco = Bloco(
                    numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco)

                incluir_bloco(bloco)

        return BLOCKCHAIN

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar a blockchain\n', error)
