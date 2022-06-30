'''
TESTE DA CLASSE MINERADOR - ATRIBUTOS E MÉTODOS
'''
from Bloco import Bloco
from Minerador import Minerador # RETIRAR ESSE IMPORT NA EXECUÇÃO

# CRIANDO MINERADORES
minerador1 = Minerador(1)
minerador2 = Minerador(2)
minerador3 = Minerador(3)
minerador4 = Minerador(4)
minerador5 = Minerador(5)

# DEFININDO VIZINHOS
minerador1.vizinhos.append(minerador2)
minerador1.vizinhos.append(minerador4)
minerador2.vizinhos.append(minerador1)
minerador2.vizinhos.append(minerador5)
minerador3.vizinhos.append(minerador1)
minerador3.vizinhos.append(minerador4)
minerador4.vizinhos.append(minerador2)
minerador4.vizinhos.append(minerador3)
minerador5.vizinhos.append(minerador3)

# CRIANDO DICIONÁRIO DE MINERADORES
dicionario_mineradores = {
    1: minerador1,
    2: minerador2,
    3: minerador3,
    4: minerador4,
    5: minerador5,
}

# CRIANDO BLOCOS PARA SEREM MINERADOS
bloco1 = Bloco(1, 'Teste bloco 1')
bloco2 = Bloco(2, 'Teste bloco 2')

# SOLICITAÇÃO DE MINERAÇÃO, PROPAGAÇÃO E ATUALIZAÇÃO
minerador1.minerar(bloco1)
minerador4.minerar(bloco2)

# IMPRIMINDO DICIONÁRIO DE MINERADORES
for k, v in dicionario_mineradores.items():
    print('- MINERADOR: {}'.format(v.identificador))
    for k1, v1 in v.blockchain.livro_razao.items():
        print('\n\t- BLOCKCHAIN')
        print('\t\t- Altura da blockchain: {}'.format(k1))
        print('\t\t- Hash anterior: {}'.format(v1.hash_anterior))
        print('\t\t- Hash próprio: {}'.format(v1.hash_proprio))
        print('------------------------------------------------------------------------------------------------------')
    for k2, v2 in v.blockchain.historico_mineradores.items():
        print('\n\t- HISTÓRICO DE MINERADORES')
        print('\t\t- Bloco Minerado: {}'.format(k2))
        print('\t\t- Minerador representante: {}'.format(v2.identificador))
        print('------------------------------------------------------------------------------------------------------')

    print('######################################################################################################\n\n')

# IMPRIMINDO ÚLTIMO BLOCO INSERIDO 
print(minerador1.blockchain.topo)

# IMPRIMINDO MINERADOR
print('\n{}'.format(minerador1))