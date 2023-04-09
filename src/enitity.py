import uuid
from enum import Enum

class Activity(Enum):
    idle = 0
    traveling = 1
    gathering_wood = 2

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