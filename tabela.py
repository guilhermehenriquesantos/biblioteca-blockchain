from prettytable import PrettyTable

from blockchain.funcoesBlockchain import importar_blockchain
from minerador.funcoesMineradores import importar_mineradores


def gerar_tabela_mineradores():
    mineradores = importar_mineradores()

    tabela = PrettyTable(
        ["ID do Minerador", "Poder computacional", "Blocos Minerados"])

    for minerador in mineradores.keys():
        tabela.add_row([minerador.identificador,
                        minerador.poder_mineracao,
                        minerador.blocos_minerados])

    print(tabela)


def gerar_tabela_blockchain():
    blockchain = importar_blockchain()

    tabela = PrettyTable(
        ["Bloco", "Dados", "Hash bloco anterior", "Nonce", "Hash deste bloco"])

    for bloco in blockchain.values():
        tabela.add_row([bloco.numero,
                        bloco.dados,
                        bloco.hash_bloco_anterior,
                        bloco.nonce,
                        bloco.hash_deste_bloco])

    print(tabela)
