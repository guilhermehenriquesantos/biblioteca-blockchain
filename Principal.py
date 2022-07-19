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
* Execução da aplicação
* Objetivo: chamar as classes responsáveis por realizar o processo de simulação de uma blockchain
*
'''
if __name__ == '__main__':
    try:
        limpar_tela()
        print('Início das minerações, aguarde...')
        persistencia = Persiste()
        tempo_inicio = time.time()

        mundo = Mundo()
        mundo.iniciar_processamento(30, 10000)

        tempo_decorrido = (time.time() - tempo_inicio)

        if (tempo_decorrido >= 60):
            tempo_decorrido = tempo_decorrido/60
            print('As minerações acabaram, tempo decorrido: {:.2f} minutos'.format(
                tempo_decorrido))
        else:
            print('As minerações acabaram, tempo decorrido: {:.2f} segundos'.format(
                tempo_decorrido))

        for miner in mundo.mineradores.keys():
            blockchain = miner.blockchain
            break

        print('\nQuantidade de minerações de forma egoísta: {}'.format(len(mundo.egoistas.mineradores_egoistas)))
        print('Quantidade de birfurcações em todo o processo: {}'.format(len(mundo.bifurcacoes)))

        persistencia.persistir_mineradores(mundo.mineradores)
        persistencia.persistir_topos(mundo.mineradores)
        persistencia.persistir_blockchain(blockchain)
        persistencia.persistir_historico(blockchain)
        persistencia.persistir_bifurcacoes(mundo)
        mundo.ordenar_poder()
        persistencia.persistir_informacoes(mundo.mineradores)

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))
