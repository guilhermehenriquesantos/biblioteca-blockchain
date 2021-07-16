import os
import random

from minerador import Minerador


MINERADORES = {}
PROBABILIDADE = random.randint(0, 100)


def cria_dicionario_mineradores():
    for identificador in range(1, 51):
        candidato_minerador = Minerador(identificador, random.randint(1, 100))
        MINERADORES[candidato_minerador.identificador] = candidato_minerador


def descobre_poder_mundial():
    poder_mundial = 0
    for minerador in MINERADORES.values():
        poder_mundial = poder_mundial + minerador.poder_mineracao
    print("\nO PODER DE MINERAÇÃO DO MUNDO É:", poder_mundial, "\n")


def define_maior_poder_mineracao():
    maior_poder = 0
    for minerador in MINERADORES.values():
        if(minerador.poder_mineracao > maior_poder):
            maior_poder = minerador.poder_mineracao

    return maior_poder


def escolhe_minerador_mais_poderoso():
    print("MINERADOR(ES) MAIS PODEROSO(S) DO MUNDO:")
    for identificador, minerador in MINERADORES.items():
        if(minerador.poder_mineracao == define_maior_poder_mineracao()):
            print("-------------------------------------")
            print("Minerador: " + str(identificador) +
                  "\t|\tPoder: " + str(minerador.poder_mineracao))
            print("-------------------------------------")


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    if (PROBABILIDADE > 10):
        cria_dicionario_mineradores()
        descobre_poder_mundial()
        escolhe_minerador_mais_poderoso()
    else:
        print("\nNão foi possível ocorrer mineração!\n")