# implementacao-blockchain

Simulação de um blockchain utilizando as tecnologias abaixo:

![Python Badge](https://img.shields.io/badge/python-3.9-blue?style=flat-square&logo=python&logoColor=white)
![Blockchain Badge](https://img.shields.io/badge/blockchain-grey?style=flat-square&logo=blockchain.com&logoColor=white)

## Funcionalidades para consenso

### Nos mineradores

1. Criar uma base de mineradores;
2. Incluir um ou mais novos mineradores na base;
3. Ordenar um minerador por seu poder;
4. Definir os vizinhos de cada minerador;
5. Descobrir o poder mundial de mineração da base criada;
6. Atualizar os mineradores em relação aos blocos inseridos na blockchain;
7. Difundir a blockchain entre os mineradores;
8. Escolher o minerador que irá minerar o novo bloco;
9. Exibir os mineradores;
10. Exportar mineradores para um arquivo CSV de nome **`mineradores.csv`**;
11. Importar mineradores de um arquivo CSV de nome **`mineradores.csv`**;
12. Criar tabela de mineradores a partir de um arquivo CSV.

### Na blockchain

1. Minerar um novo bloco fazendo referência ao bloco anterior (consegue diferenciar quando é inserido o primeiro bloco na blockchain);
2. Inclui o bloco minerado na blockchain;
3. Exibir a blockchain;
4. Importar a blockchain de um arquivo CSV de nome **`blockchain.csv`**;
5. Exportar a blockchain para um arquivo CSV de nome **`blockchain.csv`**;
6. Buscar um bloco na blockchain por meio de seu hash;
7. Buscar um determinado bloco por meio da altura que a blockchain se encontrava em sua inserção;
8. Criar uma tabela da blockchain a partir de um arquivo CSV.

## Execução

Existem duas possíveis opções para execução para deste código fonte pelo arquivo **`main.py`**:

- **Opção 1: Executar processo de mineração automático e autoexplicativo**
    - Ao executar o arquivo **`main.py`** será feita uma execução automática sem interação do usuário, ela é autoexplicativa e tem o intuito de mostrar o passo a passo que ocorre na construção de uma blockchain.

- **Opção 2: Executar milhares de minerações automáticas**
    - Ao executar o arquivo **`main.py`** será feita a mesma execução da opção 1, porém sem pausas e por milhares de vezes, simulando um processo de mineração mais realístico, começando com poucos mineradores e com o tempo este número vai aumentando, a blockchain vai ganhando mais blocos e no final você pode ver o resultado no arquivo **`blockchain.csv`** e **`mineradores.csv`**.
