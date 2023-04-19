from __future__ import annotations
import uuid
from abc import ABC, abstractmethod

import src.lib as lib

class Actor(ABC):
    uuid    : str
    _entity : lib.Mutable
    world   : lib.World


    def __init__(self,
                 uuid       : str,
                 world      : lib.World,
                 entity     : lib.Mutable) -> None:
        self.world = world
        self.entity = entity
        self.uuid = uuid
        pass

    @property
    def entity(self) -> lib.Mutable:
        return self._entity

    @entity.setter
    def entity(self,
               e  : lib.Mutable) -> None:
        assert(not e.hasActor)
        self._entity = e
        self._entity.actor = self

    @abstractmethod
    def onTick(self,
               dt   : float) -> None:
        raise NotImplementedError
    
    def toDict(self) -> dict[str,Actor]:
        return {self.uuid : self}