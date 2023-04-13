from src.ai.goap import GOAP
from src.lib.item import *
from src.lib.entity import *
from src.lib.world import *

class CollectAction(GOAP.Action):
    hasWood : bool = False
    targetPile : WoodPile | None

    def __init__(self) -> None:
        GOAP.Action.__init__(self)
        self.addPostCondition("hasWood",True)

    def reset(self):
        self.hasWood = False
        self.targetPile = None

    def isDone(self):
        return self.hasWood
    
    @property
    def requiresInRange(self) -> bool:
        return True
    
    def checkProceduralPreconditions(self, 
                                     worldObject: World, 
                                     actor : Character) -> bool:
        closest = worldObject.findClosest(actor,WoodPile)

        self.targetPile = closest
        self.target = closest
        return (closest != None)
    
    def perform(self, worldObject: World) -> bool:
        if (self.targetPile == None):
            return False
        
        if self.targetPile.inventory.contains(Wood):
            self.hasWood = True
            return True
        
        return False
