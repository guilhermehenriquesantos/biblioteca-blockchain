import os

import matplotlib.pyplot as plt
from prettytable import PrettyTable


class Persiste:
    def __init__(self, experimento, diretorio=None):
        self.experimento = experimento

        if (diretorio != None):
            self.diretorio = diretorio
        else:
            self.diretorio = './Experimentos/'

        self.estrutura = self.diretorio + self.experimento

        os.makedirs(self.estrutura, exist_ok=True)

    '''
    * Nome: persistir_mineradores
    * Parâmetros: mineradores (dicionário de mineradores)
    * Objetivo: exportar para um arquivo CSV a tabela com as análises mais relevantes referente aos mineradores.
    *
    '''
    def persistir_mineradores(self, mineradores):
        try:
            tabela = PrettyTable(['Minerador', 'Quantidade de vizinhos', 'Poder',
                                 'Blocos minerados', 'Razão blocos minerados/poder'])

            for minerador in mineradores.keys():
                quantidade_blocos = 0

                for representante in minerador.blockchain.historico_mineradores.values():
                    if (representante.identificador == minerador.identificador):
                        quantidade_blocos = quantidade_blocos + 1

                razao = quantidade_blocos/minerador.poder_computacional

                tabela.add_row([minerador.identificador,
                                len(minerador.vizinhos),
                                minerador.poder_computacional,
                                quantidade_blocos,
                                round(razao, 2)])

            dados = tabela.get_string()

            with open(self.estrutura + 'mineradores.csv', 'w') as mineradores_arquivo:
                mineradores_arquivo.write(dados)

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)

    '''
    * Nome: persistir_blockchain
    * Parâmetros: blockchain
    * Objetivo: exportar para um arquivo CSV as informações relevantes da blockchain.
    *
    '''
    def persistir_blockchain(self, blockchain):
        try:
            with open(self.estrutura + 'blockchain.csv', 'w') as blockchain_arquivo:
                for bloco in blockchain.livro_razao.values():
                    numero = bloco.numero
                    dados = bloco.dados
                    hash_anterior = bloco.hash_anterior
                    nonce = bloco.nonce
                    hash_proprio = bloco.hash_proprio

                    blockchain_arquivo.write('Número: {}\nDados: {}\nHash anterior: {}\nNonce: {}\nHash próprio: {}\n\n'.format(
                        numero,
                        dados,
                        hash_anterior,
                        nonce,
                        hash_proprio))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)

    '''
    * Nome: persistir_historico
    * Parâmetros: blockchain
    * Objetivo: exportar para um arquivo CSV as informações do minerador de cada bloco.
    *
    '''
    def persistir_historico(self, blockchain):
        try:
            tabela = PrettyTable(
                ['Hash do bloco minerado', 'Minerador que realizou a mineração'])

            for bloco, representante in blockchain.historico_mineradores.items():
                tabela.add_row([bloco,
                                representante.identificador])

            dados = tabela.get_string()

            with open(self.estrutura + 'historicoMineracao.csv', 'w') as historico_arquivo:
                historico_arquivo.write(dados)

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar o histórico de mineradores\n', error)

    '''
    * Nome: persistir_bifurcacoes
    * Parâmetros: mundo
    * Objetivo: exportar para um arquivo CSV as informações sobre ocorrência de bifurcações, como altura da blockchain que ocorreu uma bifurcação e quantas blockchains diferentes existem nessa altura. Além disso exportar um gráfico em um arquivo de imagem PNG.
    *
    '''
    def persistir_bifurcacoes(self, mundo):
        try:
            bifurcacoes = mundo.bifurcacoes.items()
            bifurcacoes = sorted(bifurcacoes)
            x, y = zip(*bifurcacoes)

            grafico, ax = plt.subplots()
            ax.plot(x, y)

            plt.title('Análise de bifurcações')
            plt.ylabel('Quantidade de bifurcações')
            plt.xlabel('Altura da blockchain')

            grafico.savefig(self.estrutura +
                            'bifurcacoes-grafico.png', format='png')

            plt.close(grafico)

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar as bifurcações\n', error)
