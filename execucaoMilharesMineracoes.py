import os
import time


from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


def execucao_milhares_mineracoes():
    start = time.time()

    MINERADORES = {}
    BLOCKCHAIN = {}

    limpar_tela()

    print('################################################')
    print('### Executando 10K de minerações, aguarde...')
    print('### Tempo estimado: 32 minutos')
    print('################################################\n')

    quantidade_blocos_inseridos = 0

    MINERADORES = criar_base_mineradores()
    MINERADORES = ordenar_minerador_por_poder(
        MINERADORES)

    for loop in range(10000):

        poder_mundial = descobrir_poder_mundial(MINERADORES)

        minerador_escolhido = escolher_minerador(
            MINERADORES, poder_mundial)

        while(minerador_escolhido == None):

            minerador_escolhido = escolher_minerador(
                MINERADORES, poder_mundial)

        ultimo_bloco = 0
        hash_bloco_anterior = None
        if (len(BLOCKCHAIN) > 0):
            ultimo_bloco = max(BLOCKCHAIN.keys())
        numero_novo_bloco = int(ultimo_bloco) + 1

        if (numero_novo_bloco > 1):
            bloco = BLOCKCHAIN.get(
                ultimo_bloco, '>>> Bloco não encontrado')
            hash_bloco_anterior = bloco.hash_deste_bloco

        quantidade_blocos_inseridos = quantidade_blocos_inseridos + 1
        dados_novo_bloco = 'Dados do bloco ' + str(quantidade_blocos_inseridos)

        novo_bloco = Bloco(numero_novo_bloco,
                           dados_novo_bloco, hash_bloco_anterior)
        BLOCKCHAIN = minerar_bloco(BLOCKCHAIN, novo_bloco)

    exportar_blockchain(BLOCKCHAIN)
    exportar_mineradores(MINERADORES)
    limpar_tela()

    total_time = (time.time() - start)

    print('##########################')
    print('### Execução concluída ###')
    print('##########################\n')

    if (total_time >= 60):
        total_time = total_time/60

        print('########################################################')
        print('### Tempo total gasto de: {:.2f} minutos'.format(total_time))
        print('########################################################\n')

    else:

        print('########################################################')
        print('### Tempo total gasto de: {:.2f} segundos'.format(total_time))
        print('########################################################\n')

    print(
        '>>>> A blockchain criada pode ser encontrada no arquivo [blockchain.csv] deste mesmo diretório')
    print(
        '>>>> O arquivo com os mineradores pode ser encontrado neste mesmo diretório, possui o nome de [mineradores.csv]')
