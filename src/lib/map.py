from __future__ import annotations
import json
import datetime
import uuid

import src.lib as lib

CHUNKSIZE = 100

class WorldChunk:
    def __init__(self,
                 uuid               : str,
                 coordinate         : lib.utils.Vector3D,
                 creationDate       : str,
                 modificationDate   : str,
                 entities           : dict[str,lib.entity.Entity]):
        """Constructor

        More text
        """
        self.uuid = uuid
        self.coordinate = coordinate
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.entities = entities
    
    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, 
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False)
        
    @classmethod
    def new(
        cls,
        coordinate  : lib.utils.Vector3D | tuple[int,int,int]):
        now = datetime.datetime.now().isoformat()
        if isinstance(coordinate,tuple):
            coordinate = lib.utils.Vector3D(coordinate[0],coordinate[1],coordinate[2])
        return cls(uuid = uuid.uuid4().__str__(),
                   coordinate = coordinate,
                   creationDate = now,
                   modificationDate = now,
                   entities = {})
    
    @classmethod
    def fromJSON(cls,
                 jsonText:str):
        params = json.loads(jsonText)
        return cls(uuid             = params["uuid"],
                   creationDate     = params["creationDate"],
                   modificationDate = params["modificationDate"],
                   entities         = params["entities"],
                   coordinate       = params["coordinate"])

    def toJSON(self):
        self.modificationDate = datetime.datetime.now().isoformat()
        return self.__str__()
    
    def toDictEntry(self):
        return {self.uuid:self}

    def inChunk(self,
                coordinate  : lib.utils.Vector3D) -> bool:
        return (coordinate.x >= self.coordinate.x) and (coordinate.x < self.coordinate.x + CHUNKSIZE) and (coordinate.y >= self.coordinate.y) and (coordinate.y < self.coordinate.y + CHUNKSIZE) 
