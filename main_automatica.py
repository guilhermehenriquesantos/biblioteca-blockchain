import os

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


MINERADORES = {}
BLOCKCHAIN = {}


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    limpar_tela()
    variavel = 0
    quantidade_testes = 0
    while variavel < 10:
        MINERADORES = criar_base_mineradores()
        MINERADORES = ordenar_minerador_por_poder(
            MINERADORES)
        print('\n>>>> Base de mineradores criada!\n')

        sleep(2)

        limpar_tela()
        exibir_mineradores(MINERADORES)

        sleep(5)

        limpar_tela()
        id = 0
        for minerador in MINERADORES.keys():
            if (int(minerador.identificador) > id):
                id = int(minerador.identificador)

        minerador_usuario = Minerador(str(id + 1), random.randint(1, 100))
        MINERADORES[minerador_usuario] = minerador_usuario.poder_mineracao
        print('\n>>>> Minerador {} de poder {} adicionado com sucesso!'.format(
            minerador_usuario.identificador, minerador_usuario.poder_mineracao))

        sleep(3)

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

        sleep(3)

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

        quantidade_testes = quantidade_testes + 1
        dados_novo_bloco = "Dados para teste " + str(quantidade_testes)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco, hash_bloco_anterior)
        BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

        print('\n>>>> O bloco {} foi inserido na blockchain\n'.format(
            novo_bloco.numero))

        sleep(3)

        limpar_tela()
        exibir_blockchain(BLOCKCHAIN)

        sleep(5)
        
        variavel = variavel + 1

    limpar_tela()
    exportar_blockchain(BLOCKCHAIN)
    print('\n>>>> Blockchain exportada com sucesso!\n')

    exportar_mineradores(MINERADORES)
    print('\n>>>> Mineradores exportados')
