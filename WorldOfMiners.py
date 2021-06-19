import random as R

from .SimpleMiner import SimpleMiner

class WorldOfMiners:

    def __init__(self,powers,F=10):
        self.miners = [SimpleMiner(i+1,powers[i]) for i in range(len(powers))]
        self.wp = sum(powers)*F


    def step(self):
        for m in self.miners:
            m.tick()
