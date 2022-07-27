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
* Parâmetros: poder_computacional
* Objetivo: os mineradores possuirão poderes computacionais iguais e a quantidade de vizinhos variadas.
*
'''
def experimento(poder_computacional):
    try:
        persistencia = Persiste('Experimento_2/')

        mundo = Mundo()
        mundo.iniciar_processamento(30, 1000, None, poder_computacional)

        for miner in mundo.mineradores.keys():
            blockchain = miner.blockchain
            break

        persistencia.persistir_mineradores(mundo.mineradores)
        persistencia.persistir_blockchain(blockchain)
        persistencia.persistir_historico(blockchain)
        persistencia.persistir_bifurcacoes(mundo)
        mundo.ordenar_poder()
        persistencia.persistir_informacoes(mundo.mineradores)

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

        print('O início do experimento dois começou, aguarde...')
        print('_______________________________________________________________')
        print('\nO experimento possui a seguinte característica: \n')
        print('2- Os mineradores possuirão poderes computacionais iguais e a quantidade de vizinhos variadas.\n')

        tempo_inicio = time.time()

        experimento(100)

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
