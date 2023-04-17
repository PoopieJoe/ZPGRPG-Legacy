from __future__ import annotations
import json
import datetime
import uuid

import src.lib as lib

class WorldHex:
    def __init__(self,
                 coordinate     : lib.utils.HexCoordinate):
        """Constructor

        More text
        """
        self.coordinate = coordinate

    @classmethod
    def new(cls,
            coordinate      : lib.utils.HexCoordinate):
        return cls(coordinate = coordinate)

    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, 
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False)
    
    # @classmethod
    # def fromJSON(cls,
    #              jsonText:str):
    #     params = json.loads(jsonText)
    #     return cls(coordinate = params["coordinate"],
    #                entities = params["entities"])

    def toJSON(self):
        self.modificationDate = datetime.datetime.now().isoformat()
        return self.__str__()


class WorldChunk:
    def __init__(self,
                 uuid            :str,
                 creationDate    :str,
                 modificationDate:str,
                 hexes           :list[WorldHex]):
        """Constructor

        More text
        """
        self.uuid = uuid
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.hexes = hexes
    
    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, 
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False)
        
    @classmethod
    def new(
        cls,
    ):
        now = datetime.datetime.now().isoformat()
        hexes = [WorldHex.new(lib.utils.HexCoordinate.new(0,0)),
                 WorldHex.new(lib.utils.HexCoordinate.new(0,1)),
                 WorldHex.new(lib.utils.HexCoordinate.new(1,1)),
                 WorldHex.new(lib.utils.HexCoordinate.new(1,0)),
                 WorldHex.new(lib.utils.HexCoordinate.new(0,-1)),
                 WorldHex.new(lib.utils.HexCoordinate.new(-1,-1)),
                 WorldHex.new(lib.utils.HexCoordinate.new(-1,0)),]
        return cls(uuid = uuid.uuid4().__str__(),
                   creationDate = now,
                   modificationDate = now,
                   hexes = hexes)
    
    @classmethod
    def fromJSON(cls,
                 jsonText:str):
        params = json.loads(jsonText)
        return cls(uuid = params["uuid"],
                   creationDate = params["creationDate"],
                   modificationDate = params["modificationDate"],
                   hexes = params["hexes"])

    def toJSON(self):
        self.modificationDate = datetime.datetime.now().isoformat()
        return self.__str__()
    
    def toDictEntry(self):
        return {self.uuid:self}


