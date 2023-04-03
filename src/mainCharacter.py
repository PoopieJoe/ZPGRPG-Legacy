import uuid
import json

from src.utils import HexCoordinate,Entity

class MainCharacter(Entity):
    def __init__(
        self,
        uuid:str,
        position:HexCoordinate
    ):
        """Constructor

        More text
        """
        Entity.__init__(self,uuid)
        self.position = position
        return
    
    @classmethod
    def new(
        cls
    ):
        return cls(
            uuid=uuid.uuid4().__str__(),
            position=HexCoordinate.new(0,0)
        )
    
    @classmethod
    def fromJSON(
        cls,
        jsonText:str
    ):
        params = json.loads(jsonText)
        return cls(
            uuid = params["uuid"],
            position = params["position"]
        )

    def toJSON(
        self,
    ):
        return self.__str__()