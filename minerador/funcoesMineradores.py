import random

from minerador.minerador import Minerador



def incluir_minerador(dicionario_mineradores, candidato_minerador):
    dicionario_mineradores[candidato_minerador] = candidato_minerador.poder_mineracao
    return dicionario_mineradores


def criar_base_mineradores():
    dicionario_mineradores = {}
    for identificador in range(1, 51):
        candidato_minerador = Minerador(identificador, random.randint(1, 100))
        dicionario_mineradores = incluir_minerador(dicionario_mineradores, candidato_minerador)

    return dicionario_mineradores


def ordenar_minerador_por_poder(dicionario_mineradores):
    dicionario_mineradores = {key: value for key, value in sorted(
        dicionario_mineradores.items(), key=lambda item: item[1])}

    return dicionario_mineradores


def descobrir_poder_mundial(dicionario_mineradores):
    poder_mundial = 0

    for minerador in dicionario_mineradores.keys():
        poder_mundial = poder_mundial + minerador.poder_mineracao

    return poder_mundial


def escolher_minerador(dicionario_mineradores, poder_mundial):
    loteria = random.randint(1, 10*poder_mundial)
    acumulado = 0
    maior_poder_minerador = 0
    minerador_final = None

    for minerador in dicionario_mineradores.keys():
        acumulado = acumulado + minerador.poder_mineracao
        if (loteria < acumulado):
            if (minerador.poder_mineracao > maior_poder_minerador):
                maior_poder_minerador = minerador.poder_mineracao
                minerador_final = minerador

    atualizar_minerador(dicionario_mineradores, minerador_final)
    return minerador_final


def atualizar_minerador(dicionario_mineradores, minerador_escolhido):
    for minerador in dicionario_mineradores.keys():
        if (minerador == minerador_escolhido):
            minerador.blocos_minerados += 1
    
    exportar_mineradores(dicionario_mineradores)


def importar_mineradores():
    try:
        dicionario_mineradores = {}
        with open('mineradores.csv', 'r') as mineradores:
            minerador = mineradores.readlines()
            for propriedades in minerador:
                detalhes = propriedades.strip().split(',')

                identificador = detalhes[0]
                poder_mineracao = detalhes[1]
                blocos_minerados = detalhes[2]

                candidato_minerador = Minerador(
                    identificador, poder_mineracao, blocos_minerados)

                incluir_minerador(candidato_minerador)

        return dicionario_mineradores

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar os mineradores\n', error)


def exportar_mineradores(dicionario_mineradores):
    try:
        with open('mineradores.csv', 'w') as mineradores:
            for minerador in dicionario_mineradores.keys():
                identificador = minerador.identificador
                poder_mineracao = minerador.poder_mineracao
                blocos_minerados = minerador.blocos_minerados

                mineradores.write('{},{},{}\n'.format(
                    identificador, poder_mineracao, blocos_minerados))

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)
