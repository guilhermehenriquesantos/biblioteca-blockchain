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
