import os

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


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


MINERADORES = {}
BLOCKCHAIN = {}


if __name__ == '__main__':
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
            MINERADORES = importar_mineradores()
            MINERADORES = ordenar_minerador_por_poder(
                MINERADORES)
            print('\n>>>> Base de mineradores importada!\n')
            escolha_menu = 'Menu de operações'

        elif (opcao_escolhida == '3' or operacao_escolhida == '1'):
            exibir_mineradores(MINERADORES)

        elif (opcao_escolhida == '4' or operacao_escolhida == '5'):
            BLOCKCHAIN = importar_blockchain()

        elif (opcao_escolhida == '5' or operacao_escolhida == '6'):
            exibir_blockchain(BLOCKCHAIN)

        elif (operacao_escolhida == '2'):
            id = 0
            for minerador in MINERADORES.keys():
                if (int(minerador.identificador) > id):
                    id = int(minerador.identificador)

            minerador_usuario = Minerador(str(id + 1), random.randint(1, 100))
            MINERADORES[minerador_usuario] = minerador_usuario.poder_mineracao
            print('\n>>>> Minerador {} de poder {} adicionado com sucesso!'.format(
                minerador_usuario.identificador, minerador_usuario.poder_mineracao))

        elif (operacao_escolhida == '3'):
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

        elif (operacao_escolhida == '4'):
            exportar_mineradores(MINERADORES)
            print('\n>>>> Mineradores exportados')

        elif (opcao_escolhida == '0' or operacao_escolhida == '0'):
            exit()

        elif (opcao_escolhida == '9' or operacao_escolhida == '9'):
            limpar_tela()

        opcao_escolhida = ''
        operacao_escolhida = ''
