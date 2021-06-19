from .SimpleMiner import SimpleMiner
from .WorldOfMiners import WorldOfMiners

if __name__=="__main__":
    world = WorldOfMiners([1,2,3,4,5,6,7])
    for w in range(100000):
        w.step()