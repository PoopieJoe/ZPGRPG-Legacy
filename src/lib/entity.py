from __future__ import annotations

from abc import ABC, abstractmethod
import src.lib as lib

class Entity(ABC):
    """Base Entity class all entities inherit from"""
    uuid           : str
    properties     : list
    position       : lib.utils.Vector3D

    def __init__(self,
                 uuid           : str,
                 properties     : list,
                 position       : lib.utils.Vector3D):
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
    
class Mutable(Entity,ABC):
    actor   : lib.actors.Actor | None
    speed   : float
    canWalk : bool
    canFly  : bool
    canSwim : bool

    def __init__(self, 
                 uuid       : str, 
                 properties : list, 
                 position   : lib.utils.Vector3D | tuple[float,float,float], 
                 speed      : float,
                 canWalk    : bool = True,
                 canFly     : bool = False,
                 canSwim    : bool = False,
                 actor      : lib.actors.Actor | None = None,):
        if isinstance(position,tuple):
            position = lib.utils.Vector3D(position[0],position[1],position[2])
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
    
    def transpose(self,
                  vector  : lib.utils.Vector3D,):
        self.position = self.position + vector
        
class Immutable(Entity,ABC):
    pass