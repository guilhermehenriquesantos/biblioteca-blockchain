import random
from minerador import Minerador


SORTEADOR = random.randint(1, 100)

if __name__ == '__main__':
    # 60% de chance
    if(SORTEADOR <= 60):
        print(Minerador(random.randint(100000000000, 999999999999), random.randint(61, 100)))
        
    # 30% de chance
    if(SORTEADOR > 60 and SORTEADOR <= 90):
        print(Minerador(random.randint(100000000000, 999999999999), random.randint(21, 60)))
        
    # 10% de chance
    if(SORTEADOR >= 90 and SORTEADOR <= 100):
        print(Minerador(random.randint(100000000000, 999999999999), random.randint(1, 20)))
        
    if(SORTEADOR == 0):
        print("Sem mineração")
    