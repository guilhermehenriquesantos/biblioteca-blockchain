import os

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    dicionario_mineradores = criar_base_mineradores()
    dicionario_mineradores = ordenar_minerador_por_poder(
        dicionario_mineradores)

    poder_mundial = descobrir_poder_mundial(dicionario_mineradores)

    minerador_escolhido = escolher_minerador(
        dicionario_mineradores, poder_mundial)

    while(minerador_escolhido == None):
        print('Ninguém teve poder suficiente para minerar um bloco nessa rodada. Escolhendo outro minerador...')
        sleep(1)
        minerador_escolhido = escolher_minerador(
            dicionario_mineradores, poder_mundial)

    limpar_tela()
    print('\nO minerador {} de poder {} está minerando\n'.format(
        minerador_escolhido.identificador, minerador_escolhido.poder_mineracao))

