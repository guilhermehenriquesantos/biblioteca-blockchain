from time import sleep
import time

from blockchain.Blockchain import *
from mineradores.Minerador import *
from conveniencias.Funcoes import *


'''
* Nome: executar_mineracao_explicativa
* Parâmetros: vazio
* Objetivo: explicar o passo a passo que ocorre no processo de mineração de um bloco na blockchain, em que é criada uma base de mineradores e dentre esses mineradores é escolhido um para minerar o próximo bloco a ser inserido na blockchain.
*           O processo de mineração é feito e o novo bloco é inserido na blockchain.
*           Após a execução de todos os processos, os arquivos referentes à blockchain e aos mineradores são exportados para o formato CSV em que o usuário pode verificar os dados.
*
'''
def executar_mineracao_explicativa():
    base_mineradores = {}
    blockchain = {}
    quantidade_blocos_inseridos = 0
    ultimo_bloco = 0
    hash_bloco_anterior = None
    id = 0

    limpar_tela()

    print('###################################')
    print('### Criando base de mineradores ###')
    print('###################################\n')
    sleep(2)
    base_mineradores = criar_base_mineradores()
    print('>>>> Base de mineradores criada!\n')
    sleep(1)
    limpar_tela()

    for loop in range(2):
        print('########################################################################')
        print('### Adicionando 2 novos mineradores na base criada no passo anterior ###')
        print('########################################################################\n')
        sleep(2)

        for minerador in base_mineradores.keys():
            if (int(minerador.identificador) > id):
                id = int(minerador.identificador)

        for m in range(1, 3):
            minerador_usuario = Minerador(str(id + 1),
                                          random.randint(1, 100))
            base_mineradores[minerador_usuario] = minerador_usuario.poder_mineracao
            print('>>>> Minerador {} de poder {} adicionado com sucesso!'.format(minerador_usuario.identificador,
                                                                                 minerador_usuario.poder_mineracao))
            id = id + 1
            sleep(1)

        limpar_tela()
        print('#####################################')
        print('### Exibindo todos os mineradores ###')
        print('#####################################\n')
        sleep(2)

        base_mineradores = ordenar_minerador_por_poder(base_mineradores)
        exibir_mineradores(base_mineradores)
        sleep(10)
        limpar_tela()

        print('############################################')
        print('### Escolhendo minerador que vai minerar ###')
        print('############################################\n')
        sleep(2)
        poder_mundial = descobrir_poder_mundial(base_mineradores)
        minerador_escolhido = definir_minerador(base_mineradores,
                                                poder_mundial)
        while(minerador_escolhido == None):
            print('>>>> Ninguém teve poder suficiente para minerar um bloco nessa rodada. Escolhendo outro minerador...')
            sleep(1)
            minerador_escolhido = definir_minerador(base_mineradores,
                                                    poder_mundial)

        print('\n>>>> O minerador {} de poder {} foi escolhido para minerar\n'.format(minerador_escolhido.identificador,
                                                                                      minerador_escolhido.poder_mineracao))
        sleep(3)
        limpar_tela()

        print('##################################')
        print('### Mineração de um novo bloco ###')
        print('##################################\n')
        sleep(2)

        if (len(blockchain) > 0):
            ultimo_bloco = max(blockchain.keys())
        numero_novo_bloco = int(ultimo_bloco) + 1

        if (numero_novo_bloco > 1):
            bloco = blockchain.get(ultimo_bloco,
                                   '>>> Bloco não encontrado')
            hash_bloco_anterior = bloco.hash_deste_bloco

        quantidade_blocos_inseridos = quantidade_blocos_inseridos + 1
        dados_novo_bloco = 'Dado do bloco ' + str(quantidade_blocos_inseridos)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco,
                           hash_bloco_anterior)

        blockchain = minerar_bloco(blockchain, novo_bloco)

        print('\n>>>> O bloco {} foi inserido na blockchain\n'.format(
            novo_bloco.numero))
        sleep(2)
        limpar_tela()

        print('###########################')
        print('### Exibindo blockchain ###')
        print('###########################\n')
        sleep(2)

        exibir_blockchain(blockchain)
        sleep(5)
        limpar_tela()

    limpar_tela()
    exportar_blockchain(blockchain)
    print('\n>>>> Blockchain exportada com sucesso!\n')
    sleep(2)

    limpar_tela()

    exportar_mineradores(base_mineradores)
    print('\n>>>> Mineradores exportados com sucesso!')
    sleep(2)
    limpar_tela()

    print('##########################')
    print('### Execução concluída ###')
    print('##########################\n')

    print(
        '>>>> A blockchain criada pode ser encontrada no arquivo [blockchain.csv] deste mesmo diretório')
    print(
        '>>>> O arquivo com os mineradores pode ser encontrado neste mesmo diretório, possui o nome de [mineradores.csv]')


'''
* Nome: execucao_baseada_realidade
* Parâmetros: vazio
* Objetivo: simular um processo realístico de mineração de uma blockchain, criando mineradores que irão minerar blocos, ao final da mineração poderá ser possível observar que os mineradores com maior poder computacional foram os que mineraram mais blocos.
*           O processo de mineração é feito e o novo bloco é inserido na blockchain.
*           Após a execução de todos os processos, os arquivos referentes à blockchain e aos mineradores são exportados para o formato CSV em que o usuário pode verificar os dados.
*
'''
def executar_mineracao_baseada_realidade():
    iniciar_contagem_tempo = time.time()
    mineradores = {}
    blockchain = {}
    quantidade_blocos_inseridos = 0
    ultimo_bloco = 0
    hash_bloco_anterior = None

    limpar_tela()

    print('################################################')
    print('### Executando 10K de minerações, aguarde...')
    print('### Tempo estimado: de 30 à 50 minutos')
    print('################################################\n')

    mineradores = criar_base_mineradores()
    mineradores = ordenar_minerador_por_poder(mineradores)
    poder_mundial = descobrir_poder_mundial(mineradores)

    for loop in range(100):
        minerador_escolhido = definir_minerador(mineradores,
                                                poder_mundial)

        while(minerador_escolhido == None):
            minerador_escolhido = definir_minerador(mineradores,
                                                    poder_mundial)

        if (len(blockchain) > 0):
            ultimo_bloco = max(blockchain.keys())

        numero_novo_bloco = int(ultimo_bloco) + 1

        if (numero_novo_bloco > 1):
            bloco = blockchain.get(ultimo_bloco,
                                   '>>> Bloco não encontrado')
            hash_bloco_anterior = bloco.hash_deste_bloco

        quantidade_blocos_inseridos = quantidade_blocos_inseridos + 1
        dados_novo_bloco = 'Dados do bloco ' + str(quantidade_blocos_inseridos)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco,
                           hash_bloco_anterior)

        blockchain = minerar_bloco(blockchain,
                                   novo_bloco)

    exportar_blockchain(blockchain)
    exportar_mineradores(mineradores)
    limpar_tela()

    tempo_decorrido = (time.time() - iniciar_contagem_tempo)

    print('##########################')
    print('### Execução concluída ###')
    print('##########################\n')

    if (tempo_decorrido >= 60):
        tempo_decorrido = tempo_decorrido/60

        print('########################################################')
        print('### Tempo total gasto de: {:.2f} minutos'.format(
            tempo_decorrido))
        print('########################################################\n')

    else:
        print('########################################################')
        print('### Tempo total gasto de: {:.2f} segundos'.format(
            tempo_decorrido))
        print('########################################################\n')

    print(
        '>>>> A blockchain criada pode ser encontrada no arquivo [blockchain.csv] deste mesmo diretório')
    print(
        '>>>> O arquivo com os mineradores pode ser encontrado neste mesmo diretório, possui o nome de [mineradores.csv]')
