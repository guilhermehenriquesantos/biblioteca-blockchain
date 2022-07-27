import random

from Egoistas import Egoista
from Minerador import Minerador


class Mundo:
    def __init__(self, mineradores={}, poder_mundial=0, bifurcacoes={}, egoistas=None):
        self.mineradores = mineradores
        self.poder_mundial = poder_mundial
        self.bifurcacoes = bifurcacoes

        if (egoistas != None):
            self.egoistas = egoistas
        else:
            self.egoistas = Egoista()

    def __str__(self):
        return 'Mundo criado com {} mineradores. Possui o poder computacional mundial da rede de {}'.format(len(self.mineradores, self.poder_mundial))

    '''
    * Nome: criar_mineradores
    * Parâmetros: próprio mundo e quantidade_mineradores (quantidade desejada de mineradores)
    * Objetivo: criar um dicionário de objetos mineradores de acordo com a quantidade informada no parâmetro do método, já definindo o poder mundial da rede e os vizinhos que cada minerador do dicionário terá.
    *
    '''
    def criar_mineradores(self, quantidade_mineradores, poder_computacional, quantidade_vizinhos):
        for identificador in range(1, quantidade_mineradores + 1):
            if (poder_computacional == None):
                novo_minerador = Minerador(
                    identificador, None, random.randint(1, 100))
            else:
                novo_minerador = Minerador(
                    identificador, None, poder_computacional)

            self.mineradores[novo_minerador] = novo_minerador.poder_computacional

        self.descobrir_poder_mundial()
        self.definir_vizinhos_minerador(quantidade_vizinhos)
        return self

    '''
    * Nome: descobrir_poder_mundial
    * Parâmetros: próprio mundo
    * Objetivo: somar todo o poder computacional dos mineradores do mundo (rede).
    *
    '''
    def descobrir_poder_mundial(self):
        for poder in self.mineradores.values():
            self.poder_mundial = self.poder_mundial + poder

        return self

    '''
    * Nome: definir_vizinhos_minerador
    * Parâmetros: próprio mundo
    * Objetivo: cada minerador terá uma quantidade de vizinhos entre um e o tamanho da rede de mineradores menos ele mesmo, então é escolhido um número aleatório de acordo com essa quantidade que representará quantos vizinhos o minerador terá. Após a escolha da quantidade, percorre-se o mundo de mineradores para definir quais os mineradores serão os vizinhos do minerador.
    *
    '''
    def definir_vizinhos_minerador(self, quantidade_definida):
        for minerador in self.mineradores.keys():
            if (quantidade_definida == None):
                quantidade_vizinhos = random.randint(
                    1, len(self.mineradores) - 1)
            else:
                quantidade_vizinhos = quantidade_definida

            for i in range(0, quantidade_vizinhos):
                vizinho_escolhido = random.choice(
                    list(self.mineradores.keys()))
                while(vizinho_escolhido.identificador == minerador.identificador and vizinho_escolhido in minerador.vizinhos):
                    vizinho_escolhido = random.choice(
                        list(self.mineradores.keys()))

                minerador.vizinhos.append(vizinho_escolhido)

        return self

    '''
    * Nome: ordenar_poder
    * Parâmetros: próprio mundo
    * Objetivo: ordena o dicionário de mineradores por poder computacional em ordem crescente.
    *
    '''
    def ordenar_poder(self):
        self.mineradores = {key: value for key, value in sorted(
            self.mineradores.items(), key=lambda item: item[1])}

        return self

    '''
    * Nome: iniciar_processamento
    * Parâmetros: próprio mundo, quantidade_mineradores (quantidade desejada de mineradores) e quantidade_blocos_desejados (tamanho da blockchain desejada para realizar o processo de mineração)
    * Objetivo: chamar os métodos necessários para criação dos mineradores que irão realizar processos de mineração e propagação até alcançarem a quantidade de blocos desejados. Após isso detectar quaisquer bifurcações na rede após minerações.
    *
    '''
    def iniciar_processamento(self, quantidade_mineradores, quantidade_blocos_desejados, quantidade_vizinhos=None, poder_computacional=None):
        self.criar_mineradores(quantidade_mineradores,
                               poder_computacional, quantidade_vizinhos)

        for minerador in self.mineradores.keys():
            while (len(minerador.blockchain.livro_razao) < quantidade_blocos_desejados):
                for minerador in self.mineradores.keys():
                    minerador.tentar_mineracao(self.poder_mundial)

                for minerador in self.mineradores.keys():
                    minerador.propagar_atualizacao(self.egoistas)

                self.detectar_bifurcacoes()

        return self

    '''
    * Nome: detectar_bifurcacoes
    * Parâmetros: próprio mundo
    * Objetivo: olhar para a rede e capturar a blockchain de maior altura, observar quantas bifurcações ela tem por meio da quantidade de mineradores que mineraram um bloco válido com a mesma altura e hash ao mesmo tempo e enviaram para seus vizinhos, após verificar essas informações deve-se retirar a duplicidade dos dados e gravar apenas a quantidade de variações da blockchain em determinada altura.
    *
    '''
    def detectar_bifurcacoes(self):
        try:
            maior_altura = 0
            bifurcacao = False
            for minerador in self.mineradores.keys():
                maior_altura = len(minerador.blockchain.livro_razao)
                if (len(minerador.blockchain.livro_razao) > maior_altura):
                    maior_altura = len(minerador.blockchain.livro_razao)

            if (maior_altura > 0):
                for minerador in self.mineradores.keys():
                    bifurcacao = False
                    blockchain_existentes = []

                    if (len(minerador.blockchain.livro_razao) == maior_altura):
                        for blockchain_comparativa in self.mineradores.keys():
                            if ((len(minerador.blockchain.livro_razao) == len(blockchain_comparativa.blockchain.livro_razao))
                                and (minerador.blockchain.topo.hash_proprio == blockchain_comparativa.blockchain.topo.hash_proprio)
                                    and (minerador.blockchain.historico_mineradores[minerador.blockchain.topo.hash_proprio].identificador != blockchain_comparativa.blockchain.historico_mineradores[blockchain_comparativa.blockchain.topo.hash_proprio].identificador)):
                                bifurcacao = True
                                blockchain_existentes.append(
                                    minerador.blockchain.historico_mineradores[minerador.blockchain.topo.hash_proprio].identificador)
                                blockchain_existentes.append(
                                    blockchain_comparativa.blockchain.historico_mineradores[blockchain_comparativa.blockchain.topo.hash_proprio].identificador)

                        if (bifurcacao):
                            blockchain_existentes = sorted(
                                set(blockchain_existentes))
                            self.bifurcacoes[len(minerador.blockchain.livro_razao)] = len(
                                blockchain_existentes)
                            return self
                        else:
                            self.bifurcacoes[len(
                                minerador.blockchain.livro_razao)] = 1
                            return self

            return self

        except Exception as error:
            print('Ocorreu um erro ao detectar as bifurcações: {}'.format(error))
            return self
