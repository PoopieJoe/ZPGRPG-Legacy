import uuid
import json
from typing import Type
import src.lib as lib

class Character(lib.entity.Mutable):
    def __init__(self,
                 uuid           : str,
                 position       : lib.utils.Vector3D | tuple[float,float,float],
                 properties     : list,
                 speed          : int):
        """Constructor

        More text
        """
        lib.entity.Mutable.__init__(self,
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
    def new(cls,
            position    : lib.utils.Vector3D | tuple[float,float,float]):
        return cls(uuid             = uuid.uuid4().__str__(),
                   position         = position,
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