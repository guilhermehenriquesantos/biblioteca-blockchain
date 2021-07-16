from bloco import Bloco


class Blockchain:
    
    def __init__(self, numero_blocos_existentes, ultimo_bloco, mecanismo_consenso):
        self.numero_blocos_existentes = numero_blocos_existentes
        self.ultimo_bloco = ultimo_bloco
        self.mecanismo_consenso = mecanismo_consenso
        
    
    def cria_bloco_inicial(self, dados_bloco):
        primeiro_bloco = Bloco(1, dados_bloco, "0000000000000000000000000000000000000000000000000000000000000000")
        primeiro_bloco = primeiro_bloco.minerar_bloco(1, dados_bloco, "0000000000000000000000000000000000000000000000000000000000000000", 4)
        return primeiro_bloco
    
    def acessar_bloco(self, hash_bloco=None, numero_bloco=None):
        pass
    
    def prova_de_trabalho():
        pass
    
    def adicionar_bloco():
        pass

