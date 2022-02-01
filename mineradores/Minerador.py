import random
import copy

from prettytable import PrettyTable

from blockchain.Blockchain import importar_blockchain


'''
* MÉTODOS ORDENADOS EM ORDEM ALFABÉTICA DE MINERADOR:
* 1 - atualizar_mineradores
* 2 - criar_base_mineradores
* 3 - definir_minerador
* 4 - definir_vizinhos
* 5 - descobrir_poder_mundial
* 6 - difundir_blockchain_recursivamente
* 7 - exibir_mineradores
* 8 - exportar_mineradores
* 9 - gerar_tabela_mineradores_csv
* 10 - importar_mineradores
* 11 - incluir_minerador
* 12 - ordenar_minerador_por_poder
'''


'''
* Nome: atualizar_mineradores
* Parâmetros:   dicionario_mineradores = dicionário que representára a base de mineradores existente
                minerador_escolhido = objeto referente ao minerador que conseguiu obter um acumulado maior do que a loteria
                hash_bloco = hash do bloco que o minerador minerou
                blockchain = recebe a blockchain completa com seu bloco inserido
* Objetivo: atualizar as informações do minerador que minerar um novo bloco na blockchain e solicitar que ele espalhe a sua atualização para os seus vizinhos que vão espalhar para os vizinhos deles.
*
'''
def atualizar_mineradores(dicionario_mineradores, minerador_escolhido, hash_bloco, blockchain):
    for minerador in dicionario_mineradores.keys():
        if (minerador == minerador_escolhido):
            receberam_blockchain_atualizada = []

            minerador.blocos_minerados.append(hash_bloco)
            minerador.blockchain = blockchain

            receberam_blockchain_atualizada.append(minerador.identificador)
            dicionario_mineradores = difundir_blockchain_recursivamente(
                minerador, receberam_blockchain_atualizada, dicionario_mineradores)

    return dicionario_mineradores


'''
* Nome: criar_base_mineradores
* Parâmetros: quantidade_mineradores = representa a quantidade de mineradores que se deseja criar
* Objetivo: criar uma base de mineradores iniciais com um identificador e um poder de mineração aletório entre 1 a 100
* Retorno: dicionário de mineradores - [key: minerador | value: poder de mineração do minerador]
*
'''
def criar_base_mineradores(quantidade_mineradores):
    dicionario_mineradores = {}

    for identificador in range(1, quantidade_mineradores):
        candidato_minerador = Minerador(identificador,
                                        random.randint(1, 100))
        dicionario_mineradores = incluir_minerador(dicionario_mineradores,
                                                   candidato_minerador)

    dicionario_base_mineradores = definir_vizinhos(dicionario_mineradores)

    return dicionario_base_mineradores


'''
* Nome: definir_minerador
* Parâmetros:   dicionario_mineradores = dicionário que representára a base de mineradores existente
                poder_mundial = valor referente ao poder de todos os mineradores somados
* Objetivo: criar um sorteio para escolher um minerador, neste sorteio tem-se uma loteria que é um valor aletório de 1 até 10 vezes o poder computacional de todos os mineradores somados. O intuito é de quanto maior for o poder computacional do minerador, maior a sua chance de minerar um novo bloco
* Retorno: o minerador escolhido para minerar o novo bloco
*
'''
def definir_minerador(dicionario_mineradores, poder_mundial):
    loteria = random.randint(1, 10*poder_mundial) # IVAN: parametrizar o 10 para facilitar os testes
    acumulado = 0

    for minerador in dicionario_mineradores.keys():
        acumulado = acumulado + minerador.poder_mineracao
        if (loteria < acumulado):
            return minerador


'''
* Nome: definir_vizinhos
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: definir quais são os mineradores vizinhos de um minerador, é criado uma cópia dos mineradores existentes, é feito um sorteio para verificar quantos vizinhos o minerador atual poderá ter (o máximo de vizinhos que ele pode ter é todos os outros mineradores existentes tirando ele), após escolher quantos vizinhos terá é feito um laço para sortear cada um dos vizinhos que esse minerador irá se conectar, ou seja, percorre-se a lista de mineradores restantes e aleatoriamente um é escolhido e após ser escolhido esse minerador não poderá ser escolhido como vizinho novamente, evitando duplicatas. Após a escolha dos vizinhos de cada minerador é preciso preencher a lista dos vizinhos dos vizinhos de cada minerador, para que seja possível o acesso ao vizinhos dos vizinhos de um minerador.
* Retorno: dicionário de mineradores com seus respectivos vizinhos, cada minerador possui no mínimo 1 vizinho.
*
'''
def definir_vizinhos(dicionario_mineradores):
    dicionario_mineradores_completo = {}

    for minerador_base in dicionario_mineradores.keys():
        dicionario_mineradores_completo[copy.deepcopy(
            minerador_base)] = minerador_base.poder_mineracao

        quantidade_vizinhos_minerador = random.randint(
            1, len(dicionario_mineradores) - 1)

        copia_dicionario_mineradores = dicionario_mineradores.copy()
        copia_dicionario_mineradores.pop(minerador_base)

        for i in range(0, quantidade_vizinhos_minerador):
            vizinho_escolhido = random.choice(
                list(copia_dicionario_mineradores.keys()))

            for minerador_efetivo in dicionario_mineradores_completo.keys():
                if (minerador_efetivo.identificador == minerador_base.identificador):
                    minerador_efetivo.vizinhos.append(vizinho_escolhido)

            copia_dicionario_mineradores.pop(vizinho_escolhido)

    copia_mineradores_completos = dicionario_mineradores_completo.copy()

    for minerador_vizinhos_incompletos in dicionario_mineradores_completo.keys():
        for vizinho in minerador_vizinhos_incompletos.vizinhos:
            for minerador_vizinhos_completos in copia_mineradores_completos.keys():
                if (vizinho.identificador == minerador_vizinhos_completos.identificador):
                    vizinho.vizinhos = minerador_vizinhos_completos.vizinhos

    return dicionario_mineradores_completo


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
* Nome: difundir_blockchain_recursivamente
* Parâmetros:   minerador = minerador que realizou a mineração para inserção de um novo bloco na blockchain;
                receberam_blockchain_atualizada = array com todos os mineradores que receberam a blockchain com o novo bloco já inserido caso não haja nenhum problema;
                dicionario_mineradores = dicionário com os mineradores sem a blockchain atualizada com o bloco novo; 
* Objetivo: atualizar todos os mineradores da blockchain com o novo bloco incluído a partir do minerador que o minerou. Esse método busca os vizinhos do minerador do bloco e informa para eles a nova blockchain e recursivamente cada um desses vizinhos vão informando os seus vizinhos da inserção de um novo bloco na blockchain caso não haja nenhuma incosistência (uma blockchain menor que a atual, uma blockchain diferente da atual, a mudança de um bloco anterior)
* Retorno: dicionário de mineradores com a nova blockchain difusa entre eles
*
'''

#IVAN: esta funcao NAO pode ser recursiva!!!! Da forma que esta a blockchain se propaga imediatamente!!!
# Cda minerador deve ter um flag "precisoPropagar"
# este flag  ligado ao minerar ou receber um blockchain
# ao propagar para os vizinhos desligue este flag
def difundir_blockchain_recursivamente(minerador, receberam_blockchain_atualizada, dicionario_mineradores):
    for vizinho in minerador.vizinhos:
        if (vizinho.identificador not in receberam_blockchain_atualizada):
            if ((vizinho.blockchain == {} or vizinho.blockchain.items() <= minerador.blockchain.items()) and len(minerador.blockchain) > len(vizinho.blockchain)):
                for minerador_desatualizado in dicionario_mineradores.keys():
                    vizinho.blockchain = minerador.blockchain
                    if (vizinho.identificador == minerador_desatualizado.identificador):
                        minerador_desatualizado.blockchain = vizinho.blockchain
                receberam_blockchain_atualizada.append(vizinho.identificador)
                difundir_blockchain_recursivamente(
                    vizinho, receberam_blockchain_atualizada, dicionario_mineradores)

            else:
                for mineradores in dicionario_mineradores.keys():
                    if (minerador.identificador == mineradores.identificador):
                        mineradores.blockchain = vizinho.blockchain

    return dicionario_mineradores


'''
* Nome: exibir_mineradores
* Parâmetros: dicionario_mineradores = dicionário que representára a base de mineradores existente
* Objetivo: mostrar na tela do usuário os mineradores existentes e suas informações mais relevantes
*
'''
def exibir_mineradores(dicionario_mineradores):
    if (len(dicionario_mineradores) == 0):
        print(
            '>>>> Ainda não temos nenhum minerador, crie ou importe sua base de mineração')
    else:
        tabela = PrettyTable(['ID do Minerador',
                              'Poder computacional',
                              'Blocos Minerados',
                              'Vizinhos',
                              'Altura da blockchain'])

        for minerador in dicionario_mineradores.keys():
            tabela.add_row([minerador.identificador,
                            minerador.poder_mineracao,
                            len(minerador.blocos_minerados),
                            len(minerador.vizinhos),
                            len(minerador.blockchain)])

        print(tabela)


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

                mineradores.write('{}|{}|{}\n'.format(identificador,
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

        tabela = PrettyTable(['1) ID do Minerador',
                              '2) Poder computacional',
                              '3) Blocos Minerados',
                              '4) Razão [3) / 2)]',
                              '5) Vizinhos do Minerador'])

        for minerador in mineradores.keys():
            razao = (len(minerador.blocos_minerados) //
                     minerador.poder_mineracao)
            vizinhos = []

            for vizinho in minerador.vizinhos:
                vizinhos.append(vizinho.identificador)

            tabela.add_row([minerador.identificador,
                            minerador.poder_mineracao,
                            len(minerador.blocos_minerados),
                            razao,
                            vizinhos])

        print(tabela)

    except Exception as error:
        print('Não foi possível gerar uma tabela, o erro apontado foi: {}'.format(error))


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
                detalhes = propriedades.strip().split('|')

                identificador = detalhes[0]
                poder_mineracao = detalhes[1]
                blocos_minerados = detalhes[2]

                identificador = int(identificador)
                poder_mineracao = int(poder_mineracao)

                blocos_minerados = blocos_minerados.replace('[', '')
                blocos_minerados = blocos_minerados.replace(']', '')
                blocos_minerados = blocos_minerados.replace("'", '')

                if (len(blocos_minerados) > 0):
                    blocos_minerados = blocos_minerados.split(', ')
                else:
                    blocos_minerados = []

                vizinhos = []
                blockchain = importar_blockchain()

                candidato_minerador = Minerador(identificador,
                                                poder_mineracao,
                                                blocos_minerados,
                                                vizinhos,
                                                blockchain)

                dicionario_mineradores = incluir_minerador(dicionario_mineradores,
                                                           candidato_minerador)

        dicionario_mineradores = definir_vizinhos(dicionario_mineradores)

        return dicionario_mineradores

    except Exception as error:
        print('\nAlgum erro ocorreu ao importar os mineradores\n', error)


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
* Classe: Minerador
* Parâmetros:   identificador = número único que representará o minerador
*               poder_mineracao = poder computacional de um minerador para minerar um bloco
*               blocos_minerados = hashes dos blocos que o minerador minerou
*               vizinhos = mineradores vizinhos ao minerador, a quem ele passa as informações dos seus blocos minerados
*               blockchain = última versão de blockchain recebida
* Objetivo: representar um objeto Minerador
*
'''
class Minerador:

    def __init__(self, identificador, poder_mineracao, blocos_minerados=[], vizinhos=[], blockchain={}):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        self.blocos_minerados = blocos_minerados
        self.vizinhos = vizinhos
        self.blockchain = blockchain

    def __str__(self):
        if (len(self.blocos_minerados) < 1):
            quantidade_blocos_minerados = 0
        else:
            quantidade_blocos_minerados = len(self.blocos_minerados)
        return '{} é um minerador com poder de mineração ({}) | Já minerou {} blocos, possui como vizinhos os mineradores [{}]'.format(self.identificador,
                                                                                                                                       self.poder_mineracao,
                                                                                                                                       quantidade_blocos_minerados,
                                                                                                                                       self.vizinhos)
