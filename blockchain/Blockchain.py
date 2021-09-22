from hashlib import sha256

from prettytable import PrettyTable


'''
* Nome: incluir_bloco
* Parâmetros:   blockchain = dicionário que representará a blockchain
*               bloco = representação de um objeto Bloco
* Objetivo: inserir um novo bloco em uma blockchain já existente
* Retorno: dicionário da blockchain - [key: número do bloco inserido | value: bloco inserido]
*
'''
def incluir_bloco(blockchain, bloco):
    blockchain[bloco.numero] = bloco
    return blockchain


'''
* Nome: minerar_bloco
* Parâmetros:   blockchain = dicionário que representará a Blockchain
*               bloco = representação de um objeto Bloco
* Objetivo: realizar o processo de mineração de acordo com as informações do bloco passado
            e inserir o novo bloco minerado na blockchain
* Retorno: dicionário da blockchain - [key: número do bloco inserido | value: bloco inserido]
*
'''
def minerar_bloco(blockchain, bloco):
    quantidade_zeros_prefixo = 4
    prefixo_hash = '0'*quantidade_zeros_prefixo
    valor_maximo_nonce = 100000000000

    if (bloco.hash_bloco_anterior == None):
        bloco.hash_bloco_anterior = '0000000000000000000000000000000000000000000000000000000000000000'

    for nonce in range(valor_maximo_nonce):
        informacoes_do_bloco = str(bloco.numero) + \
            bloco.dados + \
            bloco.hash_bloco_anterior + \
            str(nonce)

        hash_do_bloco = sha256(
            informacoes_do_bloco.encode('ascii')).hexdigest()

        bloco_minerado = Bloco(bloco.numero,
                               bloco.dados,
                               bloco.hash_bloco_anterior,
                               nonce,
                               hash_do_bloco)

        if hash_do_bloco.startswith(prefixo_hash):
            blockchain_atualizada = incluir_bloco(blockchain, bloco_minerado)
            return blockchain_atualizada

    raise BaseException(
        '\nNão foi possível realizar a mineração. Foram feitas: {valor_maximo_nonce} de tentativas\n')


'''
* Nome: exibir_blockchain
* Parâmetros: blockchain = dicionário que representará a Blockchain
* Objetivo: mostra na tela do usuário a blockchain existente no momento caso ela exista
*
'''
def exibir_blockchain(blockchain):
    if (len(blockchain) == 0):
        print(
            '>>>> Ainda não temos uma blockchain criada, crie ou importe a sua blockchain')

    else:
        tabela = PrettyTable(["Bloco",
                              "Dados",
                              "Hash bloco anterior",
                              "Nonce",
                              "Hash deste bloco"])

        for bloco in blockchain.values():
            tabela.add_row([bloco.numero,
                            bloco.dados,
                            bloco.hash_bloco_anterior,
                            bloco.nonce,
                            bloco.hash_deste_bloco])

        print(tabela)


'''
* Nome: importar_blockchain
* Parâmetros: vazio
* Objetivo: importar de um arquivo csv os dados referentes a uma blockchain criada anteriormente
* Retorno: dicionário da blockchain - [key: número do bloco inserido | value: bloco inserido]
*
'''
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

                numero_bloco = int(numero_bloco)
                nonce = int(nonce)

                bloco = Bloco(numero_bloco,
                              dados_bloco,
                              hash_bloco_anterior,
                              nonce,
                              hash_deste_bloco)

                blockchain = incluir_bloco(blockchain, bloco)

        return blockchain

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar a blockchain\n', error)


'''
* Nome: exportar_blockchain
* Parâmetros: blockchain = dicionário que representará a Blockchain
* Objetivo: exportar para um arquivo csv os dados referentes à blockchain criada no momento
*
'''
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
                    numero_bloco,
                    dados_bloco,
                    hash_bloco_anterior,
                    nonce,
                    hash_deste_bloco)
                )

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)


'''
* Nome: gerar_tabela_blockchain_csv
* Parâmetros: vazio
* Objetivo: importar blockchain de um arquivo csv e exibí-la em formato de tabela
*
'''
def gerar_tabela_blockchain_csv():
    try:
        blockchain = importar_blockchain()

        tabela = PrettyTable(["Bloco",
                            "Dados",
                            "Hash bloco anterior",
                            "Nonce",
                            "Hash deste bloco"])

        for bloco in blockchain.values():
            tabela.add_row([bloco.numero,
                            bloco.dados,
                            bloco.hash_bloco_anterior,
                            bloco.nonce,
                            bloco.hash_deste_bloco])

        print(tabela)
    except Exception as error:
        print('Não foi possível gerar uma tabela, o erro apontado foi: {}'.format(error))


'''
* Classe: Bloco
* Parâmetros:   numero = número que representará a ordem em que o bloco foi inserido na blockchain 
*               dados = conteúdo das transações do bloco 
*               hash_bloco_anterior = referência ao hash do último bloco que foi inserido na blockchain 
*               nonce = número de valor aletório escolhido para realizar a mineração do bloco 
*               hash_deste_bloco = identificador unitário do bloco na blockchain
* Objetivo: representar um objeto bloco na blockchain
*
'''
class Bloco:

    def __init__(self, numero, dados, hash_bloco_anterior=None, nonce=None, hash_deste_bloco=None):
        self.numero = numero
        self.dados = dados
        self.hash_bloco_anterior = hash_bloco_anterior
        self.nonce = nonce
        self.hash_deste_bloco = hash_deste_bloco
