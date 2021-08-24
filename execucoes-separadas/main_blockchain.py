import os

from time import sleep

from blockchain.funcoesBlockchain import *


BLOCKCHAIN = {}


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


def menu_blockchain():
    print('\n##########################################################')
    print('####################### BLOCKCHAIN #######################')
    print('##########################################################\n')
    print('Olá, essa é uma aplicação com o intuito de simular uma blockchain e nela você poderá utilizar as opções abaixo:\n')
    print('1 - Importar blockchain')
    print('2 - Minerar um novo bloco')
    print('3 - Exibir blockchain')
    print('4 - Exportar blockchain')
    print('9 - Limpar tela')
    print('0 - Sair')

    escolha = input('\nSua opção: ')

    return escolha


if __name__ == "__main__":
    limpar_tela()
    while True:
        opcao_escolhida = menu_blockchain()

        if (opcao_escolhida == '1'):
            limpar_tela()
            BLOCKCHAIN = importar_blockchain()
            print('\n>>>> Blockchain importada com sucesso!\n')

        elif (opcao_escolhida == '2'):
            limpar_tela()
            ultimo_bloco = 0
            hash_bloco_anterior = None
            if (len(BLOCKCHAIN) > 0):
                ultimo_bloco = max(BLOCKCHAIN.keys())
            numero_novo_bloco = int(ultimo_bloco) + 1

            if (numero_novo_bloco > 1):
                bloco = BLOCKCHAIN.get(
                    ultimo_bloco, '>>> Bloco não encontrado')
                hash_bloco_anterior = bloco.hash_deste_bloco

            dados_novo_bloco = input("\nDigite os dados para o novo bloco: ")

            novo_bloco = Bloco(numero_novo_bloco,
                               dados_novo_bloco, hash_bloco_anterior)
            BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

            print('\n>>>> O bloco {} foi inserido na blockchain\n'.format(
                novo_bloco.numero))

        elif (opcao_escolhida == '3'):
            limpar_tela()
            exibir_blockchain(BLOCKCHAIN)

        elif (opcao_escolhida == '4'):
            limpar_tela()
            exportar_blockchain(BLOCKCHAIN)
            print('\n>>>> Blockchain exportada com sucesso!\n')

        elif (opcao_escolhida == '9'):
            limpar_tela()

        elif (opcao_escolhida == '0'):
            exit()
