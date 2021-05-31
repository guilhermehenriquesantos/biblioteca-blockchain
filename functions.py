from hashlib import sha256
import time

MAX_NONCE = 100000000000


# MANIPULANDO BLOCKCHAIN

def ler_blockchain():
    pass


def salvar_blockchain():
    pass


def inserir_na_blockchain():
    pass


def criptografar_bloco(bloco):
    return sha256(bloco.encode('ascii')).hexdigest()


def minerar_bloco(numero_bloco, transacoes_do_bloco, hash_anterior, quantidade_zeros_prefixo):
    prefixo_hash = '0'*quantidade_zeros_prefixo

    for nonce in range(MAX_NONCE):
        bloco = str(numero_bloco) + transacoes_do_bloco + hash_anterior + str(nonce)
        hash_do_bloco = criptografar_bloco(bloco)

        if hash_do_bloco.startswith(prefixo_hash):
            return hash_do_bloco
    
    raise BaseException('\nNão foi possível realizar a mineração. Foram feitas: {MAX_NONCE} de tentativas\n')


# MANIPULANDO MINERADORES

def criar_minerador():
    pass


def sortear_minerador():
    pass


def poder_computacional_mundo():
    pass


def recompensar_minerador():
    pass


def identificar_minerador():
    pass


def razao_de_mineradores():
    pass