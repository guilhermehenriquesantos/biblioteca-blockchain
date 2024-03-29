import random

from Blockchain import Blockchain
from Minerador import Minerador


class Mundo:
    def __init__(self, mineradores={}, poder_mundial=0, bifurcacoes={}):
        self.mineradores = mineradores
        self.poder_mundial = poder_mundial
        self.bifurcacoes = bifurcacoes

    def __str__(self):
        return 'Mundo criado com {} mineradores. Possui o poder computacional mundial da rede de {}'.format(len(self.mineradores, self.poder_mundial))

    '''
    * Nome: criar_mineradores
    * Parâmetros: próprio mundo, quantidade_mineradores (quantidade desejada de mineradores), poder_computacional (quantidade de poder computacional fixa), ataque_maioria (para simulação de ataques de 51%), dimensao_ataque (porcentagem do ataque, 51%, 30%, etc.) e quantidade_fraudadores (quantidades de mineradores que irão fraudar a blockchain em um ataque)
    * Objetivo: criar um dicionário de objetos mineradores de acordo com a quantidade informada no parâmetro do método, já definindo o poder mundial da rede e os vizinhos que cada minerador do dicionário terá.
    *
    '''
    def criar_mineradores(self, quantidade_mineradores, poder_computacional, ataque_maioria, dimensao_ataque, quantidade_fraudadores):
        for identificador in range(1, quantidade_mineradores + 1):
            if (poder_computacional == None):
                novo_minerador = Minerador(
                    identificador, None, random.randint(1, 100))
            else:
                novo_minerador = Minerador(
                    identificador, None, poder_computacional)

            self.mineradores[novo_minerador] = novo_minerador.poder_computacional

        if (ataque_maioria == True):
            fraudadores = {}
            poder_fraudadores = 0

            for i in range(0, quantidade_fraudadores):
                fraudador = random.choice(list(self.mineradores.keys()))
                while (fraudador.identificador in fraudadores):
                    fraudador = random.choice(list(self.mineradores.keys()))

                fraudadores[fraudador.identificador] = fraudador

            for fraudador in fraudadores.values():
                poder_fraudadores = poder_fraudadores + fraudador.poder_computacional

            poder_mundial = (((self.descobrir_poder_mundial().poder_mundial)/10) - poder_fraudadores)

            for fraudador in fraudadores.values():
                fraudador.poder_computacional = int(((poder_mundial*(dimensao_ataque*quantidade_fraudadores)) / (1 - (dimensao_ataque*quantidade_fraudadores))) / quantidade_fraudadores) + 1
                fraudador.fraudador = True
                self.mineradores.update({fraudador:fraudador.poder_computacional})

        self.descobrir_poder_mundial()
        return self

    '''
    * Nome: descobrir_poder_mundial
    * Parâmetros: próprio mundo e fator_balanceamento
    * Objetivo: somar todo o poder computacional dos mineradores do mundo (rede) e multiplicar pelo fator de balanceamento que tem o intuito de trazer maior nivelamento entre os mineradores.
    *
    '''
    def descobrir_poder_mundial(self, fator_balanceamento=10):
        for poder in self.mineradores.values():
            self.poder_mundial = self.poder_mundial + poder

        self.poder_mundial = self.poder_mundial*fator_balanceamento
        return self

    '''
    * Nome: definir_vizinhos_minerador
    * Parâmetros: próprio mundo, quantidade_definida (quantidade de vizinhos definida para todos os mineradores)
    * Objetivo: caso não seja definido um valor específico para a quantidade de vizinhos que cada minerador terá, a quantidade de vizinhos será definida de forma randomizada entre um e o tamanho da rede de mineradores menos ele mesmo. Após a escolha da quantidade, percorre-se o mundo de mineradores para definir quais os mineradores serão os vizinhos do minerador.
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
                while(vizinho_escolhido.identificador == minerador.identificador or vizinho_escolhido in minerador.vizinhos):
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
    * Parâmetros: próprio mundo, quantidade_mineradores (quantidade desejada de mineradores), quantidade_blocos_desejados (tamanho da blockchain desejada para realizar o processo de mineração), quantidade_vizinhos (quantidade fixada para o número de vizinhos de cada minerador), poder_computacional (valor do poder computacional fixado para todos os mineradores), divisao_vizinhos (caso queira parte dos mineradores com uma definição da quantidade de vizinhos e outra parte com uma definição diferente), ataque_maioria (para possibilitar a ocorrência de ataques de 51%), dimensao_ataque (porcetagem do poder computacional que o minerador(es) terá(ão) para realizar o ataque) e quantidade_fraudadores (quantidade de mineradores que irão fraudar a blockchain em casos de ataque)
    * Objetivo: chamar os métodos necessários para criação dos mineradores que irão realizar processos de mineração e propagação até alcançarem a quantidade de blocos desejados. Após isso detectar quaisquer bifurcações na rede após minerações.
    *
    '''
    def iniciar_processamento(self, quantidade_mineradores, quantidade_blocos_desejados, quantidade_vizinhos=None, poder_computacional=None, divisao_vizinhos=None, ataque_maioria=None, dimensao_ataque=None, quantidade_fraudadores=None):
        if (self.mineradores != {}):
            for minerador in self.mineradores.keys():
                minerador.blockchain = None
                minerador.blockchain = Blockchain(minerador)
        else:
            self.criar_mineradores(quantidade_mineradores,
                                   poder_computacional, ataque_maioria, dimensao_ataque, quantidade_fraudadores)

            if (divisao_vizinhos == True):
                self.dividir_vizinhos()
            else:
                self.definir_vizinhos_minerador(quantidade_vizinhos)

        pare = False
        while (not pare):
            for minerador in self.mineradores.keys():
                minerador.tentar_mineracao(self.poder_mundial)

            for minerador in self.mineradores.keys():
                minerador.propagar_atualizacao()

            self.detectar_bifurcacoes()

            for minerador in self.mineradores.keys():
                if (len(minerador.blockchain.livro_razao) >= quantidade_blocos_desejados):
                    pare = True

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


    '''
    * Nome: dividir_vizinhos
    * Parâmetros: próprio mundo
    * Objetivo: dividir a quantidade de vizinhos entre os mineradores fazendo que parte dos mineradores terão poucos vizinhos e a outra parte terá muitos vizinhos.
    *
    '''
    def dividir_vizinhos(self):
        for minerador in self.mineradores.keys():
            if (minerador.identificador <= 25):
                for i in range(0, 40):
                    vizinho_escolhido = random.choice(list(self.mineradores.keys()))

                    while(vizinho_escolhido.identificador == minerador.identificador or vizinho_escolhido in minerador.vizinhos):
                        vizinho_escolhido = random.choice(list(self.mineradores.keys()))

                    minerador.vizinhos.append(vizinho_escolhido)
            else:
                for i in range(0, 1):
                    vizinho_escolhido = random.choice(list(self.mineradores.keys()))
                    while(vizinho_escolhido.identificador == minerador.identificador or vizinho_escolhido in minerador.vizinhos):
                        vizinho_escolhido = random.choice(
                            list(self.mineradores.keys()))

                    minerador.vizinhos.append(vizinho_escolhido)

        return self
