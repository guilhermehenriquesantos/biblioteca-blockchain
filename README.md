# implementacao-blockchain

Simulação de um blockchain utilizando as tecnologias abaixo:

![Python Badge](https://img.shields.io/badge/python-3.9-blue?style=flat-square&logo=python&logoColor=white)
![Blockchain Badge](https://img.shields.io/badge/blockchain-grey?style=flat-square&logo=blockchain.com&logoColor=white)

## Funcionalidade até o momento

### Para mineradores:

- Criar uma base de mineradores;
- Incluir um ou mais novos mineradores na base;
- Ordenar um minerador por seu poder;
- Descobrir o poder mundial de mineração;
- Escolher o minerador que irá minerar o novo bloco;
- Atualizar o número de blocos minerados do minerador que foi escolhido;
- Exibir mineradores;
- Criar tabela de mineradores a partir de um arquivo CSV;
- Exportar mineradores para um arquivo CSV de nome **`mineradores.csv`**;
- Importar mineradores de um arquivo CSV de nome **`mineradores.csv`**.

### Para a blockchain:

- Minerar um novo bloco fazendo referência ao bloco anterior (consegue diferenciar quando é inserido o primeiro bloco na blockchain);
- Inclui o bloco minerado na blockchain;
- Exibe a blockchain;
- Importa a blockchain de um arquivo CSV de nome **`blockchain.csv`**;
- Exporta a blockchain para um arquivo CSV de nome **`blockchain.csv`**.

## Execução

Existem duas possíveis opções para execução para deste código fonte pelo arquivo **`main.py`**:

- **Opção 1: Executar processo de mineração automático e autoexplicativo**
    - Ao executar o arquivo **`main.py`** será feita uma execução automática sem interação do usuário, ela é autoexplicativa e tem o intuito de mostrar o passo a passo que ocorre na construção de uma blockchain.

- **Opção 2: Executar milhares de minerações automáticas**
    - Ao executar o arquivo **`main.py`** será feita a mesma execução da opção 1, porém sem pausas e por milhares de vezes, simulando um processo de mineração mais realístico, começando com poucos mineradores e com o tempo este número vai aumentando, a blockchain vai ganhando mais blocos e no final você pode ver o resultado no arquivo **`blockchain.csv`** e **`mineradores.csv`**.
