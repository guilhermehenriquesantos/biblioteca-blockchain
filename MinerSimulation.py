import Random as R

class SimpleMiner():
  
  # also, you gonna need a counter do track mined blocks
  def __init__(self,id,power):
    
    
  # decide if this Miner mined one block
  def tick(self,difficulty):
    
    
    
class WorldOfMiners:
  
  def __init__(self,powers,F=10):
    self.miners = [SimpleMiner(i+1,powers[i]) for i in range(len(powers))]
    
    self.wp = sum(powers)*F
    
 def step(self):
    for m in self.miners:
      m.tick()
      
      
      
      
if __name__=__main__:
  world = WordlOfMiners([1,2,3,4,5,6,7])
  for _ in range(100000):
    w.step()
