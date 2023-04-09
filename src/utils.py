from typing import NamedTuple
import uuid


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
    
    