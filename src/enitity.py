import uuid
from src.utils import Enumerate

class Activity(Enumerate):
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