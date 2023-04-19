from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import NamedTuple,Callable,Iterable,Any,Literal,TypeVar
import math

class Enumerate(Enum):
    def __dict__(self):
        return {i.name: i.value for i in Enumerate}


class Vector3D(NamedTuple):        
    x:float
    y:float
    z:float
    
    
    def __neg__(self):
        return Vector3D(-self.x,
                        -self.y,
                        -self.z)

    def __sub__(self,
                other : Vector3D) -> Vector3D:
        return Vector3D(other.x-self.x,
                        other.y-self.y,
                        other.z-self.z)
    
    def __mul__(self,
                scalar : float) -> Vector3D:
        return Vector3D(scalar*self.x,
                       scalar*self.y,
                       scalar*self.z)
    
    def __add__(self,
                other : Vector3D) -> Vector3D:
        return Vector3D(other.x+self.x,
                        other.y+self.y,
                        other.z+self.z) 
    
    def distanceFrom(self,
                      other : Vector3D) -> float:
        """The Euclidian distance between any two [Point]s"""
        diff = self.__sub__(other)
        return math.sqrt(diff.x*diff.x + 
                         diff.y*diff.y + 
                         diff.z*diff.z)

class FSM(ABC):

    class FSMStates(Enum):
        pass

    state   : FSMStates

    @abstractmethod
    def updateFSM(self):
        raise NotImplementedError
    

#TODO: https://www.redblobgames.com/grids/hexagons/
# class HexCoordinate(NamedTuple):
#     q_:int
#     r_:int

#     @classmethod
#     def new(
#         cls,
#         q:int, 
#         r:int
#     ):
#         return cls(q,r)
    
#     @property
#     def s(
#         self
#     ):
#         return - (self.q_ - self.r_)
    
#     @property
#     def q(
#         self
#     ):
#         return self.q_
    
#     @property
#     def r(
#         self
#     ):
#         return self.r_
    
#     def _subtract(self,
#                   other : HexCoordinate) -> HexCoordinate:
#         return HexCoordinate(self.q - other.q,
#                              self.r - other.r)
    
#     def distanceFrom(self,
#                      other : HexCoordinate) -> float:
#         differenceVector = self._subtract(other)
#         return ( abs(differenceVector.q) + abs(differenceVector.r) + abs(differenceVector.s) ) / 2


def forEach(iterable    : Iterable,
            f           : Callable[...,None],
            condition   : Callable[...,bool] = lambda x : True):
    for i in [x for x in iterable if condition(x)]:
        f(i)