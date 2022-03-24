from os import error

from conveniencias.Funcoes import *
from ExemploExecucao import *


'''
* Execução da aplicação
* Objetivo: Chamar o exemplo de execução
*
'''
if __name__ == '__main__':
    try:
        limpar_tela()
        executar_mineracao_baseada_realidade()

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))
