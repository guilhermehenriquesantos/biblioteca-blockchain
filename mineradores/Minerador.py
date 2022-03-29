import random
import copy

from prettytable import PrettyTable

from blockchain.Blockchain import *


'''
* MÉTODOS ORDENADOS EM ORDEM ALFABÉTICA DE MINERADOR:
* 1 - atualizar_mineradores
* 2 - criar_base_mineradores
* 3 - definir_minerador
* 4 - definir_vizinhos
* 5 - descobrir_poder_mundial
* 6 - exibir_mineradores
* 7 - exportar_mineradores
* 8 - gerar_tabela_mineradores_csv
* 9 - importar_mineradores
* 10 - incluir_minerador
* 11 - ordenar_minerador_por_poder
* 12 - processar_mineracao_bifurcada
* 13 - processar_mineracao_simples
'''


'''
* Nome: atualizar_mineradores
* Parâmetros:   dicionario_mineradores = dicionário que representára a base de mineradores existente
                minerador_selecionado = objeto referente ao minerador que conseguiu obter um acumulado maior do que a loteria
                caso_de_bifurcacao = parâmetro opcional, em casos de bifurcação (fork) ele recebe o identificador do minerador "concorrente", para que caso esse minerador seja vizinho dele, não sobrescreva sua blockchain
* Objetivo: atualizar a blockchain do minerador selecionado no dicionário de mineradores principal e espalhar a blockchain minerada com o histórico de mineradores do minerador selecionado para todos os seus vizinhos que não sejam o seu concorrente na mineração do novo bloco (em caso de fork)
* Retorno: dicionário de mineradores atualizado
*
'''
def atualizar_mineradores(dicionario_mineradores, minerador_selecionado, caso_de_bifurcacao=0):
    for vizinho in minerador_selecionado.vizinhos:
        if ((len(vizinho.blockchain) < len(minerador_selecionado.blockchain)) and (vizinho.identificador != caso_de_bifurcacao)):
            vizinho.blockchain = minerador_selecionado.blockchain.copy()
            vizinho.historico_mineradores = minerador_selecionado.historico_mineradores.copy()

    for minerador in dicionario_mineradores.keys():
        if (minerador.identificador == minerador_selecionado.identificador):
            minerador = minerador_selecionado
        else:
            for vizinho in minerador_selecionado.vizinhos:
                if ((vizinho.identificador == minerador.identificador and len(vizinho.blockchain) > len(minerador.blockchain)) and (vizinho.identificador != caso_de_bifurcacao)):
                    minerador.blockchain = vizinho.blockchain
                    minerador.historico_mineradores = vizinho.historico_mineradores.copy()

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
                multiplicador = valor referência para escolher a loteria
* Objetivo: criar um sorteio para escolher um minerador, neste sorteio tem-se uma loteria que é um valor aletório de 1 até multiplicador vezes o poder computacional de todos os mineradores somados. O intuito é de quanto maior for o poder computacional do minerador, maior a sua chance de minerar um novo bloco
* Retorno: o minerador escolhido para minerar o novo bloco
*
'''
def definir_minerador(dicionario_mineradores, poder_mundial, multiplicador):
    loteria = random.randint(1, multiplicador*poder_mundial)
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
                historico_mineradores = minerador.historico_mineradores

                mineradores.write('{}|{}|{}|{}\n'.format(identificador,
                                                         poder_mineracao,
                                                         blocos_minerados,
                                                         historico_mineradores))

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

        tabela_vizinhos = PrettyTable(['1) ID do Minerador',
                                       '2) Vizinhos do Minerador'])

        for minerador in mineradores.keys():
            vizinhos = []

            for vizinho in minerador.vizinhos:
                vizinhos.append(vizinho.identificador)

            tabela_vizinhos.add_row([minerador.identificador,
                            vizinhos])

        print(tabela_vizinhos)

        tabela = PrettyTable(['1) ID do Minerador',
                              '2) Poder computacional',
                              '3) Blocos Minerados',
                              '4) Razão [Blocos Minerados / Poder]'])

        for minerador in mineradores.keys():
            razao = (len(minerador.blocos_minerados) //
                     minerador.poder_mineracao)

            tabela.add_row([minerador.identificador,
                            minerador.poder_mineracao,
                            len(minerador.blocos_minerados),
                            razao])

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
                historico_mineradores = detalhes[3]

                identificador = int(identificador)
                poder_mineracao = int(poder_mineracao)

                blocos_minerados = blocos_minerados.replace('[', '')
                blocos_minerados = blocos_minerados.replace(']', '')
                blocos_minerados = blocos_minerados.replace("'", '')

                historico_mineradores = historico_mineradores.replace('[', '')
                historico_mineradores = historico_mineradores.replace(']', '')
                historico_mineradores = historico_mineradores.replace("'", '')

                if (len(blocos_minerados) > 0):
                    blocos_minerados = blocos_minerados.split(', ')
                else:
                    blocos_minerados = []

                if (len(historico_mineradores) > 0):
                    historico_mineradores = historico_mineradores.split(', ')
                else:
                    historico_mineradores = []

                vizinhos = []
                blockchain = importar_blockchain()

                candidato_minerador = Minerador(identificador,
                                                poder_mineracao,
                                                blocos_minerados,
                                                vizinhos,
                                                blockchain,
                                                historico_mineradores)

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
* Nome: processar_mineracao_bifurcada
* Parâmetros: mineradores_escolhidos = array contendo as informações dos mineradores que irão realizar o processo de mineração ao mesmo tempo de um mesmo bloco
* Objetivo: cada minerador irá minerar um novo bloco idêntico e inserí-lo em suas blockchains, a diferença é que no histórico de mineradores cada um vai ter adicionado apenas o seu identificador como minerador do bloco e essa bifurcação somente será resolvida em uma próxima mineração
* Retorno: array com os mineradores escolhidos para minerar atualizados com as respectivas informações de cada um
*
'''
def processar_mineracao_bifurcada(mineradores_escolhidos):
    quantidade_blocos_inseridos = 0
    ultimo_bloco = 0
    hash_bloco_anterior = None

    blockchain_base = mineradores_escolhidos[0].blockchain.copy()
    if (len(mineradores_escolhidos) > 1):
        blockchain_secundaria = mineradores_escolhidos[1].blockchain.copy()

        if (blockchain_base == blockchain_secundaria):
            if (len(blockchain_base) > 0):
                ultimo_bloco = max(blockchain_base.keys())

            numero_novo_bloco = int(ultimo_bloco) + 1

            if (numero_novo_bloco > 1):
                bloco = blockchain_base.get(ultimo_bloco,
                                            '>>> Bloco não encontrado')
                hash_bloco_anterior = bloco.hash_deste_bloco

            quantidade_blocos_inseridos = len(blockchain_base) + 1
            dados_novo_bloco = 'Dados do bloco ' + \
                str(quantidade_blocos_inseridos)

            novo_bloco = Bloco(numero_novo_bloco,
                               dados_novo_bloco,
                               hash_bloco_anterior)

            blockchain_base = minerar_bloco(blockchain_base,
                                            novo_bloco)
            bloco_inserido = buscar_bloco_altura(blockchain_base, novo_bloco)

            mineradores_escolhidos[0].blockchain = blockchain_base
            mineradores_escolhidos[1].blockchain = blockchain_base

            mineradores_escolhidos[0].blocos_minerados.append(
                bloco_inserido.hash_deste_bloco)
            mineradores_escolhidos[1].blocos_minerados.append(
                bloco_inserido.hash_deste_bloco)

            mineradores_escolhidos[0].historico_mineradores.append(
                mineradores_escolhidos[0].identificador)
            mineradores_escolhidos[1].historico_mineradores.append(
                mineradores_escolhidos[1].identificador)

    return mineradores_escolhidos


'''
* Nome: processar_mineracao_simples
* Parâmetros: minerador_escolhido = contém todos as informações sobre o minerador que irá realizar o processo de mineração
* Objetivo: minerar um novo bloco e inserí-lo na blockchain do minerador selecionado para realizar o processo de mineração e atualizar seu histórico de mineradores com seu identificador
* Retorno: minerador escolhido para minerar atualizado com as novas informações após a mineração de seu novo bloco
*
'''
def processar_mineracao_simples(minerador_escolhido):
    quantidade_blocos_inseridos = 0
    ultimo_bloco = 0
    hash_bloco_anterior = None

    if (len(minerador_escolhido.blockchain) > 0):
        ultimo_bloco = max(minerador_escolhido.blockchain.keys())

    numero_novo_bloco = int(ultimo_bloco) + 1

    if (numero_novo_bloco > 1):
        bloco = minerador_escolhido.blockchain.get(ultimo_bloco,
                                                   '>>> Bloco não encontrado')
        hash_bloco_anterior = bloco.hash_deste_bloco

    quantidade_blocos_inseridos = len(minerador_escolhido.blockchain) + 1
    dados_novo_bloco = 'Dados do bloco ' + str(quantidade_blocos_inseridos)

    novo_bloco = Bloco(numero_novo_bloco,
                       dados_novo_bloco,
                       hash_bloco_anterior)

    minerador_escolhido.blockchain = minerar_bloco(minerador_escolhido.blockchain,
                                                   novo_bloco)
    bloco_inserido = buscar_bloco_altura(
        minerador_escolhido.blockchain, novo_bloco)
    minerador_escolhido.blocos_minerados.append(
        bloco_inserido.hash_deste_bloco)
    minerador_escolhido.historico_mineradores.append(
        minerador_escolhido.identificador)

    return minerador_escolhido


'''
* Classe: Minerador
* Parâmetros:   identificador = número único que representará o minerador
*               poder_mineracao = poder computacional de um minerador para minerar um bloco
*               blocos_minerados = hashes dos blocos que o minerador minerou
*               vizinhos = mineradores vizinhos ao minerador, a quem ele passa as informações dos seus blocos minerados
*               blockchain = última versão de blockchain recebida
*               historico_mineradores = contém a histórico de quem minerou cada bloco na blockchain de forma ordenada
* Objetivo: representar um objeto Minerador
*
'''
class Minerador:

    def __init__(self, identificador, poder_mineracao, blocos_minerados=[], vizinhos=[], blockchain={}, historico_mineradores=[]):
        self.identificador = identificador
        self.poder_mineracao = poder_mineracao
        self.blocos_minerados = blocos_minerados
        self.vizinhos = vizinhos
        self.blockchain = blockchain
        self.historico_mineradores = historico_mineradores

    def __str__(self):
        if (len(self.blocos_minerados) < 1):
            quantidade_blocos_minerados = 0
        else:
            quantidade_blocos_minerados = len(self.blocos_minerados)
        return '{} é um minerador com poder de mineração ({}) | Já minerou {} blocos, possui como vizinhos os mineradores [{}]'.format(self.identificador,
                                                                                                                                       self.poder_mineracao,
                                                                                                                                       quantidade_blocos_minerados,
                                                                                                                                       self.vizinhos)
