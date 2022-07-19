class Persiste:

    '''
    * Nome: persistir_mineradores
    * Parâmetros: mineradores (dicionário de mineradores)
    * Objetivo: exportar para um arquivo CSV as informações relevantes de cada minerador da rede.
    *
    '''
    def persistir_mineradores(self, mineradores):
        try:
            with open('_mineradores.csv', 'w') as mineradores_arquivo:
                for minerador in mineradores.keys():
                    identificador = minerador.identificador
                    poder_computacional = minerador.poder_computacional

                    mineradores_arquivo.write('Minerador: {}\tPoder: {}\n'.format(identificador,
                                                                                  poder_computacional
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
            with open('_blockchain.csv', 'w') as blockchain_arquivo:
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
            with open('_historicoMineracao.csv', 'w') as historico_arquivo:
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
            with open('_informacoes.csv', 'w') as informacoes:
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
    * Objetivo: exportar para um arquivo CSV as informações sobre ocorrência de bifurcações, como altura da blockchain que ocorreu uma bifurcação, bloco e mineradores envolvidos.
    *
    '''
    def persistir_bifurcacoes(self, mundo):
        try:
            with open('_bifurcacoes.csv', 'w') as bifurcacoes:
                for altura_bifurcacao, dicionario_informacoes_bifurcacao in mundo.bifurcacoes.items():
                    for hash_bloco_bifurcado, dicionario_historico_mineradores in dicionario_informacoes_bifurcacao.items():
                        array_mineradores = []
                        for minerador in dicionario_historico_mineradores.keys():
                            array_mineradores.append(minerador)
                        bifurcacoes.write('Bifurcação na altura: {}\nHash do bloco: {}\nDiferentes mineradores para o bloco: {}\n\n'.format(
                            altura_bifurcacao, hash_bloco_bifurcado, ', '.join(map(str, array_mineradores))))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar as bifurcações\n', error)

    '''
    * Nome: persistir_topos
    * Parâmetros: mineradores (dicionário de mineradores)
    * Objetivo: exportar para um arquivo CSV as informações do último bloco que cada minerador possui em sua blockchain.
    *
    '''
    def persistir_topos(self, mineradores):
        try:
            with open('_toposBlockchain.csv', 'w') as mineradores_arquivo:
                for minerador in mineradores.keys():
                    identificador = minerador.identificador
                    topo = minerador.blockchain.topo
                    numero = topo.numero
                    hash = topo.hash_proprio

                    mineradores_arquivo.write('Minerador: {}\tAltura da blockchain: {}\tÚltimo bloco: {}\n'.format(identificador,
                                                                                                                   numero,
                                                                                                                   hash
                                                                                                                   ))

        except Exception as error:
            print(
                '\nAlgum erro ocorreu ao exportar o topo da blockchain de cada minerador\n', error)
