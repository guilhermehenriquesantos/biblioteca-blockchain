from os import error
import os
import time

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
* Objetivo: Execução principal
*
'''
if __name__ == '__main__':
    try:
        limpar_tela()
        print('Início das minerações, aguarde...')
        persistencia = Persiste()
        tempo_inicio = time.time()

        mundo = Mundo()
        mundo.criar_mineradores(30)
        for k, v in mundo.mineradores.items():
            while (len(k.blockchain.livro_razao) < 10000):
                mundo.sortear_minerador(10)

        tempo_decorrido = (time.time() - tempo_inicio)
        if (tempo_decorrido >= 60):
            tempo_decorrido = tempo_decorrido/60
            print('As minerações acabaram, tempo decorrido: {:.2f} minutos'.format(tempo_decorrido))
        else:
            print('As minerações acabaram, tempo decorrido: {:.2f} segundos'.format(tempo_decorrido))
        
        for miner in mundo.mineradores.keys():
            blockchain = miner.blockchain
            break
        
        persistencia.persistir_mineradores(mundo.mineradores)
        persistencia.persistir_blockchain(blockchain)
        persistencia.persistir_historico(blockchain)
        mundo.ordenar_poder()
        persistencia.persistir_informacoes(mundo.mineradores)

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))
