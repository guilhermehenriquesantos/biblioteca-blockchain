import os
import random

from minerador import Minerador


MINERADORES = {}


def cria_dicionario_mineradores():
    for identificador in range(1, 51):
        candidato_minerador = Minerador(identificador, random.randint(1, 100))
        MINERADORES[candidato_minerador.identificador] = candidato_minerador

    return MINERADORES


def descobre_poder_mundial():
    poder_mundial = 0
    for minerador in MINERADORES.values():
        poder_mundial = poder_mundial + minerador.poder_mineracao

    return poder_mundial


def escolher_minerador():
    loteria = random.randint(1, 10*descobre_poder_mundial())
    acumulado = 0

    for minerador in MINERADORES.values():
        acumulado = acumulado + minerador.poder_mineracao

        if (loteria < acumulado and minerador.tipo_minerador == "Forte"):
            print("O minerador {} de poder {} caracterizado como um minerador do tipo {} está minerando\n".format(
                minerador.identificador, minerador.poder_mineracao, minerador.tipo_minerador))
        elif (minerador.tipo_minerador == "Mediano" and loteria < (acumulado - 1000)):
            print("O minerador {} de poder {} caracterizado como um minerador do tipo {} está minerando\n".format(
                minerador.identificador, minerador.poder_mineracao, minerador.tipo_minerador))
        elif (minerador.tipo_minerador == "Fraco" and loteria < (acumulado - 1500)):
            print("O minerador {} de poder {} caracterizado como um minerador do tipo {} está minerando\n".format(
                minerador.identificador, minerador.poder_mineracao, minerador.tipo_minerador))

    if (loteria > acumulado):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNenhum minerador foi capaz de minerar\n")


if __name__ == '__main__':
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        cria_dicionario_mineradores()

        escolher_minerador()
    except Exception as error:
        print(error)
