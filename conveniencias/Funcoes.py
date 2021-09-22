import os


'''
* Nome: limpar_tela
* Parâmetros: vazio
* Objetivo: limpar o console durante a execução
*
'''
def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


'''
* Nome: menu_execucoes
* Parâmetros: vazio
* Objetivo: exibir menu de opções para o usuário escolher o tipo de mineração que deseja realizar, um aprendizado ou simulação da realidade
*
'''
def menu_execucoes():
    print('####################################################')
    print('####################### MENU #######################')
    print('####################################################\n')
    print('Escolha a opção deseja:\n')
    print('1 - Executar processo de mineração automático e autoexplicativo')
    print('2 - Executar milhares de minerações automáticas')
    print('0 - Sair do programa')

    escolha = input('\nSua opção: ')

    return escolha
