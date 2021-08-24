import os

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


MINERADORES = {}
BLOCKCHAIN = {}


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    print('\n##########################################################')
    print('####################### BLOCKCHAIN #######################')
    print('##########################################################\n')
    print('Olá, essa é uma aplicação com o intuito de simular uma blockchain e nela você poderá utilizar as opções abaixo:\n')
    print('1 - Criar base de mineradores do zero')
    print('2 - Importar base de mineradores existente')
    print('3 - Exibir mineradores')
    print('4 - Importar blockchain existente')
    print('5 - Exibir blockchain existente')
    print('9 - Limpar tela')
    print('0 - Sair')

    escolha = input('\nSua opção: ')

    return escolha


def menu_operacoes():
    print('\n##########################################################')
    print('####################### MINERADORES ######################')
    print('##########################################################\n')
    print('Olá, essa é uma aplicação com o intuito de simular uma blockchain e nela você poderá utilizar as opções abaixo:\n')
    print('1 - Exibir mineradores')
    print('2 - Adicionar um minerador')
    print('3 - Escolher o minerador que irá minerar um bloco')
    print('4 - Exportar mineradores')
    print('5 - Importar blockchain existente')
    print('6 - Exibir blockchain existente')
    print('9 - Limpar tela')
    print('0 - Sair')

    escolha = input('\nSua opção: ')

    return escolha


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
    print('0 - Voltar ao menu anterior')

    escolha = input('\nSua opção: ')

    return escolha


if __name__ == "__main__":
    limpar_tela()
    escolha_menu = ''
    opcao_escolhida = ''
    operacao_escolhida = ''
    while True:
        if (escolha_menu == ''):
            opcao_escolhida = menu_principal()
        else:
            operacao_escolhida = menu_operacoes()

        if (opcao_escolhida == '1'):
            MINERADORES = criar_base_mineradores()
            MINERADORES = ordenar_minerador_por_poder(
                MINERADORES)
            limpar_tela()
            print('\n>>>> Base de mineradores criada!\n')
            escolha_menu = 'Menu de operações'

        elif (opcao_escolhida == '2'):
            limpar_tela()
            MINERADORES = importar_mineradores()
            MINERADORES = ordenar_minerador_por_poder(
                MINERADORES)
            print('\n>>>> Base de mineradores importada!\n')
            escolha_menu = 'Menu de operações'

        elif (opcao_escolhida == '3' or operacao_escolhida == '1'):
            limpar_tela()
            exibir_mineradores(MINERADORES)

        elif (opcao_escolhida == '4' or operacao_escolhida == '5'):
            limpar_tela()
            BLOCKCHAIN = importar_blockchain()
            print('\n>>>> Blockchain importada com sucesso!\n')

        elif (opcao_escolhida == '5' or operacao_escolhida == '6'):
            limpar_tela()
            exibir_blockchain(BLOCKCHAIN)

        elif (operacao_escolhida == '2'):
            limpar_tela()
            id = 0
            for minerador in MINERADORES.keys():
                if (int(minerador.identificador) > id):
                    id = int(minerador.identificador)

            minerador_usuario = Minerador(str(id + 1), random.randint(1, 100))
            MINERADORES[minerador_usuario] = minerador_usuario.poder_mineracao
            print('\n>>>> Minerador {} de poder {} adicionado com sucesso!'.format(
                minerador_usuario.identificador, minerador_usuario.poder_mineracao))

        elif (operacao_escolhida == '3'):
            limpar_tela()
            poder_mundial = descobrir_poder_mundial(MINERADORES)
            minerador_escolhido = escolher_minerador(
                MINERADORES, poder_mundial)
            while(minerador_escolhido == None):
                print(
                    '>>>> Ninguém teve poder suficiente para minerar um bloco nessa rodada. Escolhendo outro minerador...')
                sleep(1)
                minerador_escolhido = escolher_minerador(
                    MINERADORES, poder_mundial)

            print('\n>>>> O minerador {} de poder {} foi escolhido\n'.format(
                minerador_escolhido.identificador, minerador_escolhido.poder_mineracao))

            while True:
                opcao_blockchain = menu_blockchain()

                if (opcao_blockchain == '1'):
                    limpar_tela()
                    BLOCKCHAIN = importar_blockchain()
                    print('\n>>>> Blockchain importada com sucesso!\n')

                elif (opcao_blockchain == '2'):
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

                    dados_novo_bloco = input(
                        "\nDigite os dados para o novo bloco: ")

                    novo_bloco = Bloco(numero_novo_bloco,
                                       dados_novo_bloco, hash_bloco_anterior)
                    BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

                    print('\n>>>> O bloco {} foi inserido na blockchain\n'.format(
                        novo_bloco.numero))

                elif (opcao_blockchain == '3'):
                    limpar_tela()
                    exibir_blockchain(BLOCKCHAIN)

                elif (opcao_blockchain == '4'):
                    limpar_tela()
                    exportar_blockchain(BLOCKCHAIN)
                    print('\n>>>> Blockchain exportada com sucesso!\n')

                elif (opcao_blockchain == '9'):
                    limpar_tela()

                elif (opcao_blockchain == '0'):
                    break

        elif (operacao_escolhida == '4'):
            limpar_tela()
            exportar_mineradores(MINERADORES)
            print('\n>>>> Mineradores exportados')

        elif (opcao_escolhida == '0' or operacao_escolhida == '0'):
            exit()

        elif (opcao_escolhida == '9' or operacao_escolhida == '9'):
            limpar_tela()

        opcao_escolhida = ''
        operacao_escolhida = ''
