from typing import NamedTuple
import uuid


class Point(NamedTuple):
    x:int
    y:int

#TODO: https://www.redblobgames.com/grids/hexagons/
class HexCoordinate(NamedTuple):
    q:int
    r:int

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
        return - self.q - self.r 
    
class Entity:
    def __init__(
        self,
        uuid:str
    ):
        self.uuid = uuid

    @classmethod
    def new(
        cls
    ):
        return cls(
            uuid = uuid.uuid4().__str__()
        )