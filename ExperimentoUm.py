import os
import time
from os import error

from Mundo import Mundo
from Persistencia import Persiste

'''
* Nome: limpar_tela
* Parâmetros: vazio
* Objetivo: limpar o console durante a execução
*
'''
def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


'''
* Nome: experimento
* Parâmetros: quantidade_vizinhos
* Objetivo: os mineradores possuirão poderes computacionais variados e a mesma quantidade de vizinhos.
*
'''
def experimento(quantidade_blocos, quantidade_vizinhos):
    try:
        mundo = Mundo()
        for execucoes in range(1, 31):
            persistencia = Persiste('Experimento_1/'+str(execucoes)+'/')

            mundo.iniciar_processamento(30, quantidade_blocos, quantidade_vizinhos)

            for minerador in mundo.mineradores.keys():
                if (len(minerador.blockchain.livro_razao) >= quantidade_blocos):
                    blockchain = minerador.blockchain

            mundo.ordenar_poder()
            persistencia.persistir_mineradores(mundo.mineradores, blockchain)
            persistencia.persistir_blockchain(blockchain)
            persistencia.persistir_historico(blockchain)
            persistencia.persistir_bifurcacoes(mundo)

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))


'''
* Execução da aplicação
* Objetivo: chamar as classes responsáveis por realizar o processo de simulação de uma blockchain
*
'''
if __name__ == '__main__':
    try:
        limpar_tela()

        print('O início do experimento um começou, aguarde...')
        print('_______________________________________________________________')
        print('\nO experimento possui a seguinte característica: \n')
        print('Os mineradores possuirão poderes computacionais variados e a mesma quantidade de vizinhos.\n')

        tempo_inicio = time.time()

        experimento(10000, 5)

        tempo_decorrido = (time.time() - tempo_inicio)

        if (tempo_decorrido >= 60):
            tempo_decorrido = tempo_decorrido/60
            print('As minerações acabaram, tempo decorrido: {:.2f} minutos'.format(
                tempo_decorrido))
        else:
            print('As minerações acabaram, tempo decorrido: {:.2f} segundos'.format(
                tempo_decorrido))

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))
