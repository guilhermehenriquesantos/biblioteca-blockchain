from hashlib import sha256

from blockchain.bloco.bloco import Bloco


MAX_NONCE = 100000000000


def incluir_bloco(blockchain, bloco):
    blockchain[bloco.numero] = bloco
    return blockchain


def minerar_bloco(blockchain, bloco):
    quantidade_zeros_prefixo = 4
    prefixo_hash = '0'*quantidade_zeros_prefixo

    if (bloco.hash_bloco_anterior == None):
        bloco.hash_bloco_anterior = '0000000000000000000000000000000000000000000000000000000000000000'

    for nonce in range(MAX_NONCE):
        infos_novo_bloco = str(bloco.numero) + bloco.dados + \
            bloco.hash_bloco_anterior + str(nonce)
        hash_do_bloco = sha256(infos_novo_bloco.encode('ascii')).hexdigest()

        bloco_oficial = Bloco(bloco.numero, bloco.dados,
                              bloco.hash_bloco_anterior, nonce, hash_do_bloco)

        if hash_do_bloco.startswith(prefixo_hash):
            nova_blockchain = incluir_bloco(blockchain, bloco_oficial)
            return nova_blockchain

    raise BaseException(
        '\nNão foi possível realizar a mineração. Foram feitas: {MAX_NONCE} de tentativas\n')


def exibir_blockchain(blockchain):
    if (len(blockchain) == 0):
        print(
            '>>>> Ainda não temos uma blockchain criada, crie ou importe a sua blockchain')
    else:
        for bloco in blockchain.values():
            print('>>>> Bloco: {}\t Dados: {}\t Hash do bloco anterior: {}\t Nonce: {}\t Hash deste bloco: {}'.format(
                bloco.numero, bloco.dados, bloco.hash_bloco_anterior, bloco.nonce, bloco.hash_deste_bloco))


def importar_blockchain():
    try:
        blockchain = {}
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

                blockchain = incluir_bloco(blockchain, bloco)

        return blockchain

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar a blockchain\n', error)


def exportar_blockchain(blockchain):
    try:
        with open('blockchain.csv', 'w') as blockchain_arquivo:
            for bloco in blockchain.values():
                numero_bloco = bloco.numero
                dados_bloco = bloco.dados
                hash_bloco_anterior = bloco.hash_bloco_anterior
                nonce = bloco.nonce
                hash_deste_bloco = bloco.hash_deste_bloco

                blockchain_arquivo.write('{},{},{},{},{}\n'.format(
                    numero_bloco, dados_bloco, hash_bloco_anterior, nonce, hash_deste_bloco))

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)
