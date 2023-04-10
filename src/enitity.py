import uuid
from src.utils import Enumerate

class Activity(Enumerate):
    idle = 0
    traveling = 1
    gathering_wood = 2



class Entity:
    """Base Entity class all entities inherit from"""
    def __init__(self,
                 uuid           :str,
                 properties     :list):
        self.uuid = uuid
        self.properties = properties

    @classmethod
    def new(cls):
        return cls(uuid         = uuid.uuid4().__str__(),
                   properties   = [])
    



class WoodPile(Entity):
    def __init__(self,
                 uuid           :str,
                 properties     :list):
        Entity.__init__(self,uuid,properties)

    @classmethod
    def new(cls):
        return cls(uuid         = uuid.uuid4().__str__(),
                   properties   = ["is_wood"])