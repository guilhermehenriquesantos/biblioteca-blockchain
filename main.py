import os
import time

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


def main_automatica():
    MINERADORES = {}
    BLOCKCHAIN = {}

    def limpar_tela():
        return os.system('cls' if os.name == 'nt' else 'clear')

    limpar_tela()

    loop = 0
    quantidade_blocos_inseridos = 0

    print('###################################')
    print('### Criando base de mineradores ###')
    print('###################################\n')
    sleep(2)

    MINERADORES = criar_base_mineradores()
    print('>>>> Base de mineradores criada!\n')
    sleep(1)
    limpar_tela()

    while loop < 10:
        id = 0
        for minerador in MINERADORES.keys():
            if (int(minerador.identificador) > id):
                id = int(minerador.identificador)

        print('########################################')
        print('### Adicionando 50 novos mineradores ###')
        print('########################################\n')
        sleep(2)

        for m in range(1, 51):
            minerador_usuario = Minerador(str(id + 1), random.randint(1, 100))
            MINERADORES[minerador_usuario] = minerador_usuario.poder_mineracao
            print('>>>> Minerador {} de poder {} adicionado com sucesso!'.format(
                minerador_usuario.identificador, minerador_usuario.poder_mineracao))
            id += 1
            sleep(1)

        limpar_tela()
        print('#####################################')
        print('### Exibindo todos os mineradores ###')
        print('#####################################\n')
        sleep(2)

        MINERADORES = ordenar_minerador_por_poder(
            MINERADORES)
        exibir_mineradores(MINERADORES)
        sleep(10)
        limpar_tela()

        print('############################################')
        print('### Escolhendo minerador que vai minerar ###')
        print('############################################\n')
        sleep(2)
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
        sleep(3)
        limpar_tela()

        print('##################################')
        print('### Mineração de um novo bloco ###')
        print('##################################\n')
        sleep(2)

        ultimo_bloco = 0
        hash_bloco_anterior = None
        if (len(BLOCKCHAIN) > 0):
            ultimo_bloco = max(BLOCKCHAIN.keys())
        numero_novo_bloco = int(ultimo_bloco) + 1

        if (numero_novo_bloco > 1):
            bloco = BLOCKCHAIN.get(
                ultimo_bloco, '>>> Bloco não encontrado')
            hash_bloco_anterior = bloco.hash_deste_bloco

        quantidade_blocos_inseridos = quantidade_blocos_inseridos + 1
        dados_novo_bloco = 'Dado do bloco ' + str(quantidade_blocos_inseridos)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco, hash_bloco_anterior)
        BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

        print('\n>>>> O bloco {} foi inserido na blockchain\n'.format(
            novo_bloco.numero))
        sleep(2)

        limpar_tela()

        print('###########################')
        print('### Exibindo blockchain ###')
        print('###########################\n')
        sleep(2)

        exibir_blockchain(BLOCKCHAIN)
        sleep(5)
        limpar_tela()

        loop += 1

    limpar_tela()
    exportar_blockchain(BLOCKCHAIN)
    print('\n>>>> Blockchain exportada com sucesso!\n')
    sleep(1)

    limpar_tela()

    exportar_mineradores(MINERADORES)
    print('\n>>>> Mineradores exportados com sucesso!')
    sleep(2)
    limpar_tela()

    print('##########################')
    print('### Execução concluída ###')
    print('##########################\n')

    print(
        '>>>> A blockchain criada pode ser encontrada no arquivo [blockchain.csv] deste mesmo diretório')
    print(
        '>>>> O arquivo com os mineradores pode ser encontrado neste mesmo diretório, possui o nome de [mineradores.csv]')


def main_milhares_mineracoes():
    MINERADORES = {}
    BLOCKCHAIN = {}

    def limpar_tela():
        return os.system('cls' if os.name == 'nt' else 'clear')

    start = time.time()

    limpar_tela()

    print('#####################################################')
    print('### Executando milhares de minerações, aguarde... ###')
    print('########### Tempo estimado: 12 minutos ##############')
    print('#####################################################\n')

    loop = 0
    quantidade_blocos_inseridos = 0

    MINERADORES = criar_base_mineradores()

    while loop < 1000:
        id = 0
        for minerador in MINERADORES.keys():
            if (int(minerador.identificador) > id):
                id = int(minerador.identificador)

        for m in range(1, 51):
            minerador_usuario = Minerador(str(id + 1), random.randint(1, 100))
            MINERADORES[minerador_usuario] = minerador_usuario.poder_mineracao
            id += 1

        MINERADORES = ordenar_minerador_por_poder(
            MINERADORES)

        poder_mundial = descobrir_poder_mundial(MINERADORES)

        minerador_escolhido = escolher_minerador(
            MINERADORES, poder_mundial)

        while(minerador_escolhido == None):

            minerador_escolhido = escolher_minerador(
                MINERADORES, poder_mundial)

        ultimo_bloco = 0
        hash_bloco_anterior = None
        if (len(BLOCKCHAIN) > 0):
            ultimo_bloco = max(BLOCKCHAIN.keys())
        numero_novo_bloco = int(ultimo_bloco) + 1

        if (numero_novo_bloco > 1):
            bloco = BLOCKCHAIN.get(
                ultimo_bloco, '>>> Bloco não encontrado')
            hash_bloco_anterior = bloco.hash_deste_bloco

        quantidade_blocos_inseridos = quantidade_blocos_inseridos + 1
        dados_novo_bloco = 'Dado do bloco ' + str(quantidade_blocos_inseridos)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco, hash_bloco_anterior)
        BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

        loop += 1

    exportar_blockchain(BLOCKCHAIN)
    exportar_mineradores(MINERADORES)
    limpar_tela()

    total_time = str((time.time() - start))

    print('##########################')
    print('### Execução concluída ###')
    print('##########################\n')

    print('########################################################')
    print('### Tempo total gasto de: {} segundos'.format(total_time))
    print('########################################################\n')

    print(
        '>>>> A blockchain criada pode ser encontrada no arquivo [blockchain.csv] deste mesmo diretório')
    print(
        '>>>> O arquivo com os mineradores pode ser encontrado neste mesmo diretório, possui o nome de [mineradores.csv]')


def main_interativa():
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
                        '\nDigite os dados para o novo bloco: ')

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


def menu_execucoes():
    print('####################################################')
    print('####################### MENU #######################')
    print('####################################################\n')
    print('Escolha a opção deseja:\n')
    print('1 - Executar processo de mineração automático e autoexplicativo')
    print('2 - Executar milhares de minerações automáticas')
    print('3 - Interagir criando minha própria blockchain')

    escolha = input('\nSua opção: ')

    return escolha


if __name__=='__main__':
    escolha_usuario = menu_execucoes()
    
    if (escolha_usuario == '1'):
        main_automatica()
    elif (escolha_usuario == '2'):
        main_milhares_mineracoes()
    elif (escolha_usuario == '3'):
        main_interativa()
    else:
        print('Escolha uma opção válida, saindo do programa...')
        exit()