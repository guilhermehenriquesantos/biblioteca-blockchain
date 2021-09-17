import os
import time

from time import sleep

from blockchain.funcoesBlockchain import *
from minerador.funcoesMineradores import *

from execucaoAutomatica import *
from execucaoInterativa import *
from execucaoMilharesMineracoes import *


def menu_execucoes():
    print('####################################################')
    print('####################### MENU #######################')
    print('####################################################\n')
    print('Escolha a opção deseja:\n')
    print('1 - Executar processo de mineração automático e autoexplicativo')
    print('2 - Executar milhares de minerações automáticas')
    # print('3 - Interagir criando minha própria blockchain')

    escolha = input('\nSua opção: ')

    return escolha


if __name__=='__main__':
    limpar_tela()
    escolha_usuario = menu_execucoes()
    
    if (escolha_usuario == '1'):
        execucao_automatica()
    elif (escolha_usuario == '2'):
        execucao_milhares_mineracoes()
    # elif (escolha_usuario == '3'):
        # execucao_interativa()
    else:
        limpar_tela()
        print('Escolha uma opção válida, saindo do programa...')
        exit()