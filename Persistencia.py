class Persiste:

    def persistir_mineradores(self, mineradores):
        try:
            with open('mineradores.csv', 'w') as mineradores_arquivo:
                for minerador in mineradores.keys():
                    identificador = minerador.identificador
                    poder_computacional = minerador.poder_computacional

                    mineradores_arquivo.write('Minerador: {} \tPoder: {}\n'.format(identificador,
                                                                                   poder_computacional
                                                                                   ))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)

    def persistir_blockchain(self, blockchain):
        try:
            with open('blockchain.csv', 'w') as blockchain_arquivo:
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

    def persistir_historico(self, blockchain):
        try:
            with open('historicoMineracao.csv', 'w') as historico_arquivo:
                for bloco, representante in blockchain.historico_mineradores.items():
                    hash_bloco = bloco
                    minerador = representante.identificador

                    historico_arquivo.write('Bloco minerado: {}\tMinerador: {}\n'.format(hash_bloco,
                                                                                         minerador))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar a blockchain\n', error)

    def persistir_informacoes(self, mineradores):
        try:
            with open('informacoes.csv', 'w') as informacoes:
                for minerador in mineradores.keys():
                    quantidade_blocos = 0
                    identificador = minerador.identificador
                    poder_computacional = minerador.poder_computacional
                    for representante in minerador.blockchain.historico_mineradores.values():
                        if (representante.identificador == minerador.identificador):
                            quantidade_blocos = quantidade_blocos + 1

                    razao = quantidade_blocos//poder_computacional

                    informacoes.write('Minerador: {} \tPoder: {}\tQuantidade blocos minerados: {}\t Razão: {}\n'.format(identificador,
                                                                                                                        poder_computacional,
                                                                                                                        quantidade_blocos,
                                                                                                                        razao
                                                                                                                        ))

        except Exception as error:
            print('\nAlgum erro ocorreu ao exportar os mineradores\n', error)
