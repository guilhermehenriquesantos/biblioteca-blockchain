class Blockchain:
    def __init__(self, representante, livro_razao=None, topo=None, historico_mineradores=None, fraudada=False):
        self.representante = representante

        if (livro_razao != None):
            self.livro_razao = {key: value for key, value in sorted(
                livro_razao.items(), key=lambda item: item[0])}
            self.topo = self.livro_razao.get(max(self.livro_razao))
        else:
            self.livro_razao = {}
            self.topo = topo

        if (historico_mineradores != None):
            self.historico_mineradores = historico_mineradores
        else:
            self.historico_mineradores = {}

        self.fraudada = fraudada

    def __str__(self):
        return 'Minerador detentor da blockchain: {}\n'.format(self.representante.identificador)

    '''
    * Nome: atualizar
    * Parâmetros: própria blockchain e blockchain_atualizada (blockchain com os novos dados a serem inseridos)
    * Objetivo: verificar os dados faltantes em uma blockchain honesta e completar com os dados da blockchain mais atualizada.
    *
    '''
    def atualizar(self, blockchain_atualizada):
        try:
            if (blockchain_atualizada.fraudada == False):
                self.livro_razao = blockchain_atualizada.livro_razao.copy()
                self.historico_mineradores = blockchain_atualizada.historico_mineradores.copy()
                self.topo = self.livro_razao.get(max(self.livro_razao))

            return self
        except Exception as error:
            print('Não foi possível atualizar a blockchain, erro: {}'.format(error))
            return self

    '''
    * Nome: inserir
    * Parâmetros: própria blockchain e bloco
    * Objetivo: inserir um novo bloco no livro razão da blockchain, atualizar o último bloco do topo da blockchain, atualizar o histórico de mineradores com o hash do bloco minerado e o minerador representante desse bloco, por fim, se o bloco a ser inserido foi fraudado, sinalizar a blockchain como fraudada.
    *
    '''
    def inserir(self, bloco):
        self.livro_razao[bloco.numero] = bloco
        self.topo = bloco
        self.historico_mineradores[bloco.hash_proprio] = self.representante

        if (bloco.fraudado == True):
            self.fraudada = True

        return self

    '''
    * Nome: ordenar
    * Parâmetros: própria blockchain
    * Objetivo: ordenar o livro razão pelo número do bloco.
    *
    '''
    def ordenar(self):
        self.livro_razao = {key: value for key, value in sorted(
            self.livro_razao.items(), key=lambda item: item[0])}

        return self
