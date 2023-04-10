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
    
    def s(
        self
    ):
        return - (self.q_ - self.r_)
    
    def q(
        self
    ):
        return self.q_
    
    def r(
        self
    ):
        return self.r_
    
class Action:
    preconditions   : dict
    postconditions  : dict
    cost            : float

    def __init__(self,
                    preconditions   : dict,
                    postconditions  : dict,
                    cost            : float) -> None:
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.cost = cost
        pass

class Actions(Enum):
    goto = Action(preconditions   = {},
                  postconditions  = {},
                  cost            = 0)
    
    gatherWood = Action(preconditions   = {"wood in range":True},
                        postconditions  = {"has wood":True},
                        cost            = 100)

def forEach(iterable    : Iterable,
            f           : Callable[...,None],
            condition   : Callable[...,bool] = lambda x : True):
    for i in [x for x in iterable if condition(x)]:
        f(i)