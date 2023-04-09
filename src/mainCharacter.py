import uuid
import json

from src.enitity import Entity,Activity
from src.utils import HexCoordinate

class MainCharacter(Entity):
    def __init__(self,
                 uuid        :str,
                 position    :HexCoordinate,
                 activity    :Activity):
        """Constructor

        More text
        """
        Entity.__init__(self,uuid)
        self.position = position
        self.activity = activity
        return
    
    # def __str__(self):
    #     return json.dumps(self,
    #                       default=lambda o: o.__dict__, 
    #                       sort_keys=True,
    #                       indent=4,
    #                       ensure_ascii=False)
    
    @classmethod
    def new(cls):
        return cls(uuid=uuid.uuid4().__str__(),
                   position=HexCoordinate.new(0,0),
                   activity=Activity.idle)
    
    @classmethod
    def fromJSON(cls,
                 jsonText:str):
        params = json.loads(jsonText)
        return cls(uuid        = params["uuid"],
                   position    = params["position"],
                   activity    = params["activity"])

    def toJSON(self):
        return self.__str__()