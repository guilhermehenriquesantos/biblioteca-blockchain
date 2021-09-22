import random

from prettytable import PrettyTable


'''
* Nome: incluir_minerador
* Parâmetros:   dicionario_mineradores = dicionário que representará os mineradores
*               candidato_minerador = representação de um objeto Minerador
* Objetivo: inserir um novo minerador na base de mineradores já existente
* Retorno: dicionário de mineradores - [key: minerador | value: poder de mineração do minerador]
*
'''
def incluir_minerador(dicionario_mineradores, candidato_minerador):
    dicionario_mineradores[candidato_minerador] = candidato_minerador.poder_mineracao
    return dicionario_mineradores


'''
* Nome: criar_base_mineradores
* Parâmetros: vazio
* Objetivo: criar uma base de 30 mineradores iniciais com um identificador e um poder de mineração aletório entre 1 a 100
* Retorno: dicionário de mineradores - [key: minerador | value: poder de mineração do minerador]
*
'''
def criar_base_mineradores():
    dicionario_mineradores = {}

    for identificador in range(1, 31):
        candidato_minerador = Minerador(identificador,
                                        random.randint(1, 100))
        dicionario_mineradores = incluir_minerador(dicionario_mineradores,
                                                   candidato_minerador)

    return dicionario_mineradores


'''
* Nome: ordenar_minerador_por_poder
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: ordenar os mineradores por ordem crescente de seus poderem
* Retorno: dicionário de mineradores - [key: minerador | value: poder de mineração do minerador]
*
'''
def ordenar_minerador_por_poder(dicionario_mineradores):
    dicionario_mineradores = {key: value for key, value in sorted(
        dicionario_mineradores.items(), key=lambda item: item[1])}

    return dicionario_mineradores


'''
* Nome: descobrir_poder_mundial
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: somar o valor do poder de mineração de todos os mineradores existentes na base
* Retorno: valor referente ao poder de todos os mineradores somados 
*
'''
def descobrir_poder_mundial(dicionario_mineradores):
    poder_mundial = 0

    for minerador in dicionario_mineradores.keys():
        poder_mundial = poder_mundial + minerador.poder_mineracao

    return poder_mundial


'''
* Nome: definir_minerador
* Parâmetros:   dicionario_mineradores = dicionário que representára a base de mineradores existente
                poder_mundial = valor referente ao poder de todos os mineradores somados
* Objetivo: criar um sorteio para escolher um minerador, neste sorteio tem-se uma loteria que é um valor aletório de 1 até 10 vezes o poder computacional de todos os mineradores somados. O intuito é de quanto maior for o poder computacional do minerador, maior a sua chance de minerar um novo bloco
* Retorno: o minerador escolhido para minerar o novo bloco
*
'''
def definir_minerador(dicionario_mineradores, poder_mundial):
    loteria = random.randint(1, 10*poder_mundial)
    acumulado = 0

    for minerador in dicionario_mineradores.keys():
        acumulado = acumulado + minerador.poder_mineracao
        if (loteria < acumulado):
            atualizar_minerador(dicionario_mineradores, minerador)

            return minerador


'''
* Nome: atualizar_minerador
* Parâmetros:   dicionario_mineradores = dicionário que representára a base de mineradores existente
                minerador_escolhido = objeto referente ao minerador que conseguiu obter um acumulado maior do que a loteria
* Objetivo: atualizar o número de blocos minerados do minerador escolhido para minerar
*
'''
def atualizar_minerador(dicionario_mineradores, minerador_escolhido):
    for minerador in dicionario_mineradores.keys():
        if (minerador == minerador_escolhido):
            minerador.blocos_minerados = minerador.blocos_minerados + 1


'''
* Nome: exibir_mineradores
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: mostrar na tela do usuário os mineradores existentes
*
'''
def exibir_mineradores(dicionario_mineradores):
    if (len(dicionario_mineradores) == 0):
        print(
            '>>>> Ainda não temos nenhum minerador, crie ou importe sua base de mineração')
    else:
        tabela = PrettyTable(['ID do Minerador',
                              'Poder computacional',
                              'Blocos Minerados'])

        for minerador in dicionario_mineradores.keys():
            tabela.add_row([minerador.identificador,
                            minerador.poder_mineracao,
                            minerador.blocos_minerados])

        print(tabela)


'''
* Nome: importar_mineradores
* Parâmetros: vazio
* Objetivo: importar de um arquivo csv os dados referentes aos mineradores criados anteriormente
* Retorno: dicionário de mineradores - [key: minerador | value: poder de mineração do minerador]
*
'''
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

                identificador = int(identificador)
                poder_mineracao = int(poder_mineracao)
                blocos_minerados = int(blocos_minerados)

                candidato_minerador = Minerador(identificador,
                                                poder_mineracao,
                                                blocos_minerados)

                dicionario_mineradores = incluir_minerador(dicionario_mineradores,
                                                           candidato_minerador)

        return dicionario_mineradores

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar os mineradores\n', error)


'''
* Nome: exportar_mineradores
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: exportar para um arquivo csv os dados referentes aos mineradores criados
*
'''
def exportar_mineradores(dicionario_mineradores):
    try:
        with open('mineradores.csv', 'w') as mineradores:
            for minerador in dicionario_mineradores.keys():
                identificador = minerador.identificador
                poder_mineracao = minerador.poder_mineracao
                blocos_minerados = minerador.blocos_minerados

                mineradores.write('{},{},{}\n'.format(identificador,
                                                      poder_mineracao,
                                                      blocos_minerados))

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)


'''
* Nome: gerar_tabela_mineradores_csv
* Parâmetros: vazio
* Objetivo: importar mineradores de um arquivo csv e exibí-los em formato de tabela
*
'''
def gerar_tabela_mineradores_csv():
    try:
        mineradores = importar_mineradores()

        tabela = PrettyTable(['ID do Minerador',
                            'Poder computacional',
                            'Blocos Minerados'])

        for minerador in mineradores.keys():
            tabela.add_row([minerador.identificador,
                            minerador.poder_mineracao,
                            minerador.blocos_minerados])

        print(tabela)

    except Exception as error:
        print('Não foi possível gerar uma tabela, o erro apontado foi: {}'.format(error))


'''
* Classe: Minerador
* Parâmetros:   identificador = número único que representará o minerador
*               poder_mineracao = poder computacional de um minerador para minerar um bloco
*               blocos_minerados = quantidade de blocos que um minerador minerou
* Objetivo: representar um objeto Minerador
*
'''
class Minerador:

    def __init__(self, identificador, poder_mineracao, blocos_minerados=0):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        self.blocos_minerados = blocos_minerados

    def __str__(self):
        return '{} é um minerador com poder de mineração ({}) | Já minerou {} blocos'.format(self.identificador,
                                                                                             self.poder_mineracao,
                                                                                             self.blocos_minerados)
