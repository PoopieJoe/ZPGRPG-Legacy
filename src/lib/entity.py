from __future__ import annotations

from abc import ABC, abstractmethod
from src.lib.utils import Enumerate,HexCoordinate
from src.lib.actors import Actor

class Entity(ABC):
    """Base Entity class all entities inherit from"""
    uuid           : str
    properties     : list
    position       : HexCoordinate

    def __init__(self,
                 uuid           : str,
                 properties     : list,
                 position       : HexCoordinate):
        self.uuid = uuid
        self.properties = properties
        self.position = position

    @property
    def needsActor(self):
        return False
    
    def toDict(self) -> dict[str,Entity]:
        return {self.uuid : self}

    # @classmethod
    # def new(cls):
    #     return cls(uuid         = uuid.uuid4().__str__(),
    #                properties   = [],
    #                position     = HexCoordinate(0,0))
    
class Movable(Entity,ABC):
    actor   : Actor | None
    speed   : int
    canWalk : bool
    canFly  : bool
    canSwim : bool

    def __init__(self, 
                 uuid       : str, 
                 properties : list, 
                 position   : HexCoordinate, 
                 speed      : int,
                 canWalk    : bool = True,
                 canFly     : bool = False,
                 canSwim    : bool = False,
                 actor      : Actor | None = None,):
        super().__init__(uuid, 
                         properties, 
                         position,)
        self.actor = actor
        self.speed = speed
        self.canWalk = canWalk
        self.canFly = canFly
        self.canSwim = canSwim

    @property
    def hasActor(self) -> bool:
        return self.actor != None
        
    @property
    def needsActor(self):
        return False
        
class Immovable(Entity,ABC):
    pass