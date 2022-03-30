# biblioteca-blockchain

Biblioteca peso-leve em Python para auxiliar na simulação de operações em blockchain. Tecnologias utilizadas:

![Python Badge](https://img.shields.io/badge/python-3.9-blue?style=flat-square&logo=python&logoColor=white)
![Blockchain Badge](https://img.shields.io/badge/blockchain-grey?style=flat-square&logo=blockchain.com&logoColor=white)

## Processos executados

1. Prova de trabalho;
2. Consenso;
3. Bifurcações.

### Nos mineradores

1. Criar uma base de mineradores;
2. Incluir um ou mais novos mineradores na base;
3. Ordenar um minerador por seu poder;
4. Definir os vizinhos de cada minerador;
5. Descobrir o poder mundial de mineração da base criada;
6. Chamar o processo de mineração para um ou dois mineradores;
7. Espalhar a blockchain de um minerador para seus vizinhos;
8. Permitir bifurcações;
9.  Exibir os mineradores;
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

**1.** Cria um dicionário para representar os mineradores (30 mineradores no total)<br>
**2.** Ordena esses mineradores por poder computacional<br>
**3.** Descobre o poder computacional de todos os mineradores<br>
**4.** Irá executar 10000 minerações e em cada uma, terá a probabilidade de 0,1% de ocorrência de uma bifurcação (fork)<br>
**5.** Nos casos que não ocorre bifurcações (forks):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.1.** Criação de um array que irá armazenar os mineradores que receberam a blockchain mais atualizada daquela rodada<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.2.** Escolha do minerador que irá minerar um novo bloco<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.3.** Realizar o processo de mineração de um novo bloco, atualizando o minerador escolhido para minerar com seu novo bloco inserido na blockchain<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.4.** Atualizar apenas os vizinhos desse minerador com a nova blockchain e informando os vizinhos que o minerador escolhido minerou um novo bloco<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.5.** Procurar em todos os mineradores, os que possuem a blockchain atualizada e inserí-los no array de mineradores que já possuem a blockchain com maior prova de trabalho<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.6.** Enquanto tiver mineradores desatualizados da atualização da blockchain, é verificado quem já possui a blockchain atualizada e que ainda não passou para seu vizinhos, são notificados para enviarem a nova atualização da blockchain e todos os mineradores que recebem a nova versão, entram no array de quem recebeu a nova versão da blockchain<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.7.** Atualizo o dicionário de mineradores com os mineradores atualizados<br>
**6.** Nos casos que ocorrem a bifurcação (fork):<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.1.** Criação de um array que irá armazenar os mineradores que receberam a blockchain mais atualizada daquela rodada<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.2.** Criação de um array que irá armazenar os mineradores escolhidos para minerar<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.3.** Escolha dos dois mineradores que irão minerar ao mesmo tempo<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.4.** Adicionar mineradores escolhidos no array que possuirá os mineradores escolhidos<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.5.** Realização do processo de mineração, os dois mineradores escolhidos irão minerar ao mesmo tempo o mesmíssimo bloco<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.6.** Cada minerador irá atualizar somente seus vizinhos dessa atualização<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.7.** Enquanto tiver mineradores desatualizados em relação à altura (prova de trabalho) da blockchain mais atualizada, cada minerador que possui uma blockchain com a altura atualizada irá propagar a sua própria blockchain, fazendo com que ocorra uma bifurcação com uma parte dos mineradores possuindo a blockchain que um minerador propagou e a outra parte com a blockchain de mesma altura do outro minerador escolhido para minerar<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.8.** Atualizo o dicionário de mineradores com os mineradores atualizados<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.9.** Anotação da altura em que ocorreu a bifurcação<br>
**7.** Exportação da blockchain atualizada<br>
**8.** Exportação dos mineradores<br>
**9.** Exibida tabela de razão entre poder computacional e blocos minerados<br>
**10.** Exibida quantidade de bifurcações e altura da blockchain em que ocorreram<br>