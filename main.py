import random
from minerador import Minerador


MINERADORES = {}


if __name__ == '__main__':
    maior_poder = 0
    poder_mundial = 0

    # Criando o array dos mineradores
    for identificador in range(1, 51):
        candidato_minerador = Minerador(identificador, random.randint(1, 100))
        MINERADORES[candidato_minerador.identificador] = candidato_minerador

    # Olhando o poder mundial
    # Escolhendo o maior poder entre os mineradores
    for identificador, minerador in MINERADORES.items():
        poder_mundial = poder_mundial + minerador.poder_mineracao

        if(minerador.poder_mineracao > maior_poder):
            maior_poder = minerador.poder_mineracao

    print("\nO PODER DE MINERAÇÃO DO MUNDO É:", poder_mundial, "\n")
    print("MINERADOR(ES) MAIS PODEROSO(S) DO MUNDO:")

    # Definindo os mineradores com maior poder de mineração
    for identificador, minerador in MINERADORES.items():
        if(minerador.poder_mineracao == maior_poder):
            print("-------------------------------------")
            print("Minerador: " + str(identificador) +
                  "\t|\tPoder: " + str(minerador.poder_mineracao))
            print("-------------------------------------")
