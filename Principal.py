from os import error

from conveniencias.Funcoes import *
from TiposExecucoes import *


'''
* Execução da aplicação
* Objetivo: chamar os tipos de execuções existentes
*
'''
if __name__ == '__main__':
    try:
        limpar_tela()
        escolha_usuario = menu_execucoes()

        if (escolha_usuario == '1'):
            executar_mineracao_explicativa()

        elif (escolha_usuario == '2'):
            executar_mineracao_baseada_realidade()

        elif (escolha_usuario == '0'):
            limpar_tela()
            print('Saindo da aplicação...')
            exit()

        else:
            limpar_tela()
            print('Escolha uma opção válida, fechando aplicação...')
            exit()

    except Exception as error:
        print('Ocorreu o erro: {}'.format(error))
