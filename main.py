import random
from minerador import Minerador


SORTEADOR = random.randint(1, 100)
MINERADORES = {}
MINERADOR = {}


if __name__ == '__main__':

    for candidatar in range(0, 50):
        candidato_minerador = Minerador(random.randint(
            100000000000, 999999999999), random.randint(1, 100))
        MINERADORES[candidato_minerador.identificador] = candidato_minerador.poder_mineracao

    maior_poder = 0

    for identificador, poder_mineracao in MINERADORES.items():
        if(poder_mineracao > maior_poder):
            maior_poder = poder_mineracao

    for identificador, poder_mineracao in MINERADORES.items():
        if(poder_mineracao == maior_poder):
            MINERADOR[identificador] = poder_mineracao

    for identificador, poder_mineracao in MINERADOR.items():
        print("-------------------------------------")
        print("Minerador: " + str(identificador) +
              "\t| Poder: " + str(poder_mineracao))
        print("-------------------------------------")
