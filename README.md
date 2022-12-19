# biblioteca-blockchain

Esse trabalho de conclusão de curso visa realizar a criação de biblioteca open source que permita a realização de simulações realísticas para uma blockchain, possibilitando a execução de diferentes processos que comumente ocorrem em uma rede baseada em um sistema blockchain.

![Python Badge](https://img.shields.io/badge/python-3.9-blue?style=flat-square&logo=python&logoColor=white)
![Blockchain Badge](https://img.shields.io/badge/blockchain-grey?style=flat-square&logo=blockchain.com&logoColor=white)

## Processos executados

1. Criação de uma base de mineradores;
2. Definição dos vizinhos de cada minerador;
3. Tentativa de mineração dos mineradores que irão realizar o processo para minerar;
4. Realização do processo de mineração utilizando o algoritmo para obtenção de consenso por meio de prova de trabalho (PoW);
5. Atualização da blockchain do minerador e repasse para seus vizinhos;
6. Verificação de ocorrências de bifurcações;
7. Possibilidade para exploração de vulnerabilidades;
8. Informações relevantes exportadas para arquivos em formato CSV e gráficos em PNG.

## Procedimentos de configuração de ambiente

1. Instale o Git: `sudo apt install git`
2. Instale o Python 3.9: 
    * Atualize a lista de pacotes e instale os pré-requisitos: 
        - `sudo apt update`
        - `sudo apt install software-properties-common`
	* Adicione o PPA deadsnakes à lista de fontes do seu sistema e quando solicitado, pressione [Enter] para continuar: 
        - `sudo add-apt-repository ppa:deadsnakes/ppa`
	* Depois que o repositório estiver ativado, você poderá instalar o Python 3.9 executando:
        - `sudo apt install python3.9`
	* Verifique se a instalação foi bem-sucedida digitando:
        - `python3.9 --version`

    Para demais dúvidas, o link abaixo poder dar um bom suporte: [How to Install Python 3.9 on Ubuntu 20.04](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
3. Instalar o PIP:
    * Tente executar o comando: `python3.9 -m pip install -U pip`
    * Caso não dê certo a primeira maneira, tente realizar a segunda digitando os seguintes comandos:
        - `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
	    - `sudo apt install python3.9-distutils`
	    - `python3.9 get-pip.py`
4. Instalar matplotlib: 
    - Tente executar o comando: `python3.9 -m pip install -U matplotlib`
    - Se não funcionar, use o comando: `python3.9 -m pip install matplotlib --force-reinstall`
5. Instalar prettytable:
    - Tente executar o comando: `python3.9 -m pip install -U prettytable`
    - Se não funcionar, use o comando: `python3.9 -m pip install prettytable --force-reinstall`

## Procedimentos de instalação e execução

1. Faça o clone do projeto em sua máquina;
2. Execute os arquivos **`Principal.py`**, **`ExperimentoUm.py`**, **`ExperimentoDois.py`**, **`ExperimentoTres`** e **`ExperimentoQuatro`**;
3. Observe a simulação de uma blockchain baseada na realidade. Esse processo pode demorar de acordo com a quantidade de blocos desejada, quanto mais blocos, maior o tempo de espera.

### Agradecimentos

Muito obrigado por acompanhar esse repositório, a qualquer momento, podem surgir novidades.
