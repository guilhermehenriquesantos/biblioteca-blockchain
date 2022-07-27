import os

import matplotlib.pyplot as plt


class Persiste:
    def __init__(self, experimento, diretorio=None):
        self.experimento = experimento

        if (diretorio != None):
            self.diretorio = diretorio
        else:
            self.diretorio = './resultados/'

        self.estrutura = self.diretorio + self.experimento

        os.makedirs(self.estrutura, exist_ok=True)

    '''
    * Nome: persistir_mineradores
    * Parâmetros: mineradores (dicionário de mineradores)
    * Objetivo: exportar para um arquivo CSV as informações relevantes de cada minerador da rede.
    *
    '''
    def persistir_mineradores(self, mineradores):
        try:
            with open(self.estrutura + 'mineradores.csv', 'w') as mineradores_arquivo:
                for minerador in mineradores.keys():
                    identificador = minerador.identificador
                    poder_computacional = minerador.poder_computacional
                    quantidade_vizinhos = len(minerador.vizinhos)

                    mineradores_arquivo.write('Minerador: {}\tPoder: {}\tQuantidade de vizinhos {}\n'.format(identificador,
                                                                                                             poder_computacional,
                                                                                                             quantidade_vizinhos
                                                                                                             ))

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
            with open(self.estrutura + 'historicoMineracao.csv', 'w') as historico_arquivo:
                for bloco, representante in blockchain.historico_mineradores.items():
                    hash_bloco = bloco
                    minerador = representante.identificador

                    historico_arquivo.write('Bloco minerado: {}\tMinerador: {}\n'.format(hash_bloco,
                                                                                         minerador))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar o histórico de mineradores\n', error)

    '''
    * Nome: persistir_informacoes
    * Parâmetros: mineradores (dicionário de mineradores)
    * Objetivo: exportar para um arquivo CSV a influência que o poder computacional tem sobre quantidade de blocos que um minerador irá minerar.
    *
    '''
    def persistir_informacoes(self, mineradores):
        try:
            with open(self.estrutura + 'informacoes.csv', 'w') as informacoes:
                for minerador in mineradores.keys():
                    quantidade_blocos = 0
                    identificador = minerador.identificador
                    poder_computacional = minerador.poder_computacional
                    for representante in minerador.blockchain.historico_mineradores.values():
                        if (representante.identificador == minerador.identificador):
                            quantidade_blocos = quantidade_blocos + 1

                    razao = quantidade_blocos/poder_computacional

                    informacoes.write('Minerador: {}\tPoder: {}\tQuantidade blocos minerados: {}\tRazão: {:.2f}\n'.format(identificador,
                                                                                                                          poder_computacional,
                                                                                                                          quantidade_blocos,
                                                                                                                          razao
                                                                                                                          ))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar as informações\n', error)

    '''
    * Nome: persistir_bifurcacoes
    * Parâmetros: mundo
    * Objetivo: exportar para um arquivo CSV as informações sobre ocorrência de bifurcações, como altura da blockchain que ocorreu uma bifurcação e quantas blockchains diferentes existem nessa altura. Além disso exportar um gráfico em um arquivo de imagem PNG.
    *
    '''
    def persistir_bifurcacoes(self, mundo):
        try:
            with open(self.estrutura + 'bifurcacoes.csv', 'w') as bifurcacoes:
                for altura_bifurcacao, quantidade_blockchains in mundo.bifurcacoes.items():
                    bifurcacoes.write('Bifurcação na altura: {}\tQuantidade de blockchains existentes: {}\n'.format(
                        altura_bifurcacao, quantidade_blockchains))

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
