import time

from blockchain.Blockchain import *
from conveniencias.Funcoes import *
from mineradores.Minerador import *

'''
* Nome: execucao_baseada_realidade
* Parâmetros: vazio
* Objetivo: executar funções das classes Minerador e Blockchain para simular um processo realístico de mineração
* Execução: a ordem de execução está detalhada no README.md
*
'''
def executar_mineracao_baseada_realidade():
    iniciar_contagem_tempo = time.time()
    mineradores = {}
    flag_bifurcacao = []

    limpar_tela()

    print('################################################')
    print('### Executando 10K de minerações, aguarde...')
    print('### Tempo estimado: 30 minutos ou mais')
    print('################################################\n')

    mineradores = criar_base_mineradores(31)
    mineradores = ordenar_minerador_por_poder(mineradores)
    poder_mundial = descobrir_poder_mundial(mineradores)

    for loop in range(10000):
        probabilidade_fork = random.randint(1, 1000)

        if (probabilidade_fork == 1):
            receberam_blockchain_atualizada = []
            mineradores_escolhidos = []

            primeiro_minerador_escolhido = definir_minerador(
                mineradores, poder_mundial, 10)
            while(primeiro_minerador_escolhido == None):
                primeiro_minerador_escolhido = definir_minerador(
                    mineradores, poder_mundial, 10)

            segundo_minerador_escolhido = definir_minerador(
                mineradores, poder_mundial, 10)
            while(segundo_minerador_escolhido == None or segundo_minerador_escolhido == primeiro_minerador_escolhido):
                segundo_minerador_escolhido = definir_minerador(
                    mineradores, poder_mundial, 10)

            mineradores_escolhidos.append(primeiro_minerador_escolhido)
            mineradores_escolhidos.append(segundo_minerador_escolhido)

            mineradores_escolhidos = processar_mineracao_bifurcada(
                mineradores_escolhidos)

            for miner in mineradores_escolhidos:
                if (miner.identificador == primeiro_minerador_escolhido.identificador):
                    mineradores = atualizar_mineradores(
                        mineradores, miner, segundo_minerador_escolhido.identificador)
                elif (miner.identificador == segundo_minerador_escolhido.identificador):
                    mineradores = atualizar_mineradores(
                        mineradores, miner, primeiro_minerador_escolhido.identificador)

                altura_blockchain = len(miner.blockchain)

                for minerador in mineradores.keys():
                    if (len(minerador.blockchain) == altura_blockchain):
                        receberam_blockchain_atualizada.append(
                            minerador.identificador)

                dicionario_mineradores = mineradores.copy()

                while(len(mineradores) > len(receberam_blockchain_atualizada)):
                    for minerador in mineradores.keys():
                        if (len(minerador.blockchain) == altura_blockchain and minerador.identificador != primeiro_minerador_escolhido.identificador and minerador.identificador != segundo_minerador_escolhido.identificador):
                            dicionario_mineradores = atualizar_mineradores(
                                dicionario_mineradores, minerador)
                            for vizinho in minerador.vizinhos:
                                if (vizinho.identificador not in receberam_blockchain_atualizada):
                                    receberam_blockchain_atualizada.append(
                                        vizinho.identificador)

                mineradores = dicionario_mineradores

            flag_bifurcacao.append(
                'Bifurcação na altura: ' + str(altura_blockchain))

        else:
            receberam_blockchain_atualizada = []

            minerador_selecionado = definir_minerador(
                mineradores, poder_mundial, 10)
            while(minerador_selecionado == None):
                minerador_selecionado = definir_minerador(
                    mineradores, poder_mundial, 10)

            minerador_selecionado = processar_mineracao_simples(
                minerador_selecionado)

            mineradores = atualizar_mineradores(
                mineradores, minerador_selecionado)

            for minerador in mineradores.keys():
                if (len(minerador.blockchain) == len(minerador_selecionado.blockchain)):
                    receberam_blockchain_atualizada.append(
                        minerador.identificador)

            dicionario_mineradores = mineradores.copy()

            while(len(mineradores) > len(receberam_blockchain_atualizada)):
                for minerador in mineradores.keys():
                    if (len(minerador.blockchain) == len(minerador_selecionado.blockchain)):
                        dicionario_mineradores = atualizar_mineradores(
                            dicionario_mineradores, minerador)
                        for vizinho in minerador.vizinhos:
                            if (vizinho.identificador not in receberam_blockchain_atualizada):
                                receberam_blockchain_atualizada.append(
                                    vizinho.identificador)

            mineradores = dicionario_mineradores

    for minerador in mineradores.keys():
        blockchain = minerador.blockchain
        break

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

    gerar_tabela_mineradores_csv()

    if (len(flag_bifurcacao) > 0):
        print('\n>>>> Número total de bifurcações ocorridas foi {}, em:\n'.format(
        len(flag_bifurcacao)))
        for bifurcacoes in flag_bifurcacao:
            print(bifurcacoes)
    else:
        print('\n>>>> Não ocorreu nenhuma bifurcação no processo de mineração\n')