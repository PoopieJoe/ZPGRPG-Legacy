import uuid
import json
from typing import Type
import src.lib as lib

class Character(lib.entity.Movable):
    def __init__(self,
                 uuid           : str,
                 position       : lib.utils.HexCoordinate,
                 properties     : list,
                 speed          : int):
        """Constructor

        More text
        """
        lib.entity.Movable.__init__(self,
                                    uuid,
                                    properties,
                                    position,
                                    speed)
        return
    
    @property
    def needsActor(self):
        return True
    
    # def __str__(self):
    #     return json.dumps(self,
    #                       default=lambda o: o.__dict__, 
    #                       sort_keys=True,
    #                       indent=4,
    #                       ensure_ascii=False)
    
    @classmethod
    def new(cls):
        return cls(uuid             = uuid.uuid4().__str__(),
                   position         = lib.utils.HexCoordinate.new(0,0),
                   properties       = [],
                   speed            = 1)
    
    

    # @classmethod
    # def fromJSON(cls,
    #              jsonText:str):
    #     params = json.loads(jsonText)
    #     return cls(uuid         = params["uuid"],
    #                position     = params["position"],
    #                activity     = params["activity"],
    #                properties   = params["properties"])

    # def toJSON(self):
    #     return self.__str__()