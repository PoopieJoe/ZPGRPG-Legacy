from __future__ import annotations
from enum import Enum
from typing import NamedTuple,Callable,Iterable
import uuid

class Enumerate(Enum):
    def __dict__(self):
        return {i.name: i.value for i in Enumerate}

class Point(NamedTuple):
    x:int
    y:int

#TODO: https://www.redblobgames.com/grids/hexagons/
class HexCoordinate(NamedTuple):
    q_:int
    r_:int

    @classmethod
    def new(
        cls,
        q:int, 
        r:int
    ):
        return cls(q,r)
    
    @property
    def s(
        self
    ):
        return - (self.q_ - self.r_)
    
    @property
    def q(
        self
    ):
        return self.q_
    
    @property
    def r(
        self
    ):
        return self.r_
    
    def _subtract(self,
                  other : HexCoordinate) -> HexCoordinate:
        return HexCoordinate(self.q - other.q,
                             self.r - other.r)
    
    def distanceFrom(self,
                     other : HexCoordinate) -> float:
        differenceVector = self._subtract(other)
        return ( abs(differenceVector.q) + abs(differenceVector.r) + abs(differenceVector.s) ) / 2


def forEach(iterable    : Iterable,
            f           : Callable[...,None],
            condition   : Callable[...,bool] = lambda x : True):
    for i in [x for x in iterable if condition(x)]:
        f(i)