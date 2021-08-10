import os
import random

from time import sleep
from minerador.minerador import Minerador


def cria_dicionario_mineradores():
    mineradores = {}

    for identificador in range(1, 51):
        candidato_minerador = Minerador(identificador, random.randint(1, 100))
        mineradores[candidato_minerador] = candidato_minerador.poder_mineracao

    return mineradores


def descobre_poder_mundial(dicionario_mineradores):
    poder_mundial = 0

    for minerador in dicionario_mineradores.keys():
        poder_mundial = poder_mundial + minerador.poder_mineracao

    return poder_mundial


def ordenar_minerador_por_poder(dicionario_mineradores):
    dicionario_mineradores = {key: value for key, value in sorted(
        dicionario_mineradores.items(), key=lambda item: item[1])}

    return dicionario_mineradores


def escolher_minerador(dicionario_mineradores):
    loteria = random.randint(
        1, 10*descobre_poder_mundial(dicionario_mineradores))
    acumulado = 0
    maior_poder_minerador = 0
    minerador_final = None

    for minerador in dicionario_mineradores.keys():
        acumulado = acumulado + minerador.poder_mineracao
        if (loteria < acumulado):
            if (minerador.poder_mineracao > maior_poder_minerador):
                maior_poder_minerador = minerador.poder_mineracao
                minerador_final = minerador

    return minerador_final


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    try:
        limpar_tela()

        mineradores = cria_dicionario_mineradores()
        mineradores_ordenados = ordenar_minerador_por_poder(mineradores)
        minerador_escolhido = escolher_minerador(mineradores_ordenados)

        while(minerador_escolhido == None):
            print('Ninguém teve poder suficiente para minerar um bloco nessa rodada. Escolhendo outro minerador...')
            sleep(1)
            minerador_escolhido = escolher_minerador(mineradores_ordenados)

        limpar_tela()
        print('\nO minerador {} de poder {} está minerando\n'.format(
            minerador_escolhido.identificador, minerador_escolhido.poder_mineracao))

    except Exception as error:
        print(error)
