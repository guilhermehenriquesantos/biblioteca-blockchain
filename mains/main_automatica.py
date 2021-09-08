import os

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


MINERADORES = {}
BLOCKCHAIN = {}


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
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
