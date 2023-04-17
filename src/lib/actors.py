from __future__ import annotations
import uuid
from abc import ABC, abstractmethod

import src.lib as lib

class Actor(ABC):
    uuid    : str
    _entity : lib.entity.Movable
    world   : lib.world.World

    def __init__(self,
                 uuid       : str,
                 world      : lib.world.World,
                 entity     : lib.entity.Movable) -> None:
        self.world = world
        self.entity = entity
        self.uuid = uuid
        pass

    @property
    def entity(self) -> lib.entity.Movable:
        return self._entity

    @entity.setter
    def entity(self,
               e  : lib.entity.Movable) -> None:
        assert(not e.hasActor)
        self._entity = e
        self._entity.actor = self

    @abstractmethod
    def onTick(self) -> None:
        raise NotImplementedError
    
    def toDict(self) -> dict[str,Actor]:
        return {self.uuid : self}