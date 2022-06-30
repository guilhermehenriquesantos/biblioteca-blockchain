class Blockchain:
    def __init__(self, representante, livro_razao=None, topo=None, historico_mineradores=None):
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

    def __str__(self):
        return 'Minerador detentor da blockchain: {}\n'.format(self.representante.identificador)

    def atualizar(self, blockchain_atualizada):
        try:
            for key, value in blockchain_atualizada.livro_razao.items():
                if (key not in self.livro_razao.keys()):
                    self.livro_razao[key] = value

            for key, value in blockchain_atualizada.historico_mineradores.items():
                if (key not in self.historico_mineradores.keys()):
                    self.historico_mineradores[key] = value

            self.ordenar()
            self.topo = self.livro_razao.get(max(self.livro_razao))

            return self
        except Exception as error:
            print('Não foi possível atualizar a blockchain, erro: {}'.format(error))
            return self

    def inserir(self, bloco):
        self.livro_razao[bloco.numero] = bloco
        self.topo = bloco
        self.historico_mineradores[bloco.hash_proprio] = self.representante

        return self

    def ordenar(self):
        self.livro_razao = {key: value for key, value in sorted(
            self.livro_razao.items(), key=lambda item: item[0])}

        return self
