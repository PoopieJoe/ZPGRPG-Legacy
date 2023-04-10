"""world package

more text
"""
import io
import json
import datetime
import uuid

from typing import Type,TypeVar
from src.utils import HexCoordinate,Actions
from src.enitity import Entity,WoodPile
from src.mainCharacter import MainCharacter

WORLDFOLDER = "../saves"



class WorldHex:
    def __init__(self,
                 coordinate     : HexCoordinate,
                 entities       : dict[str,Entity]):
        """Constructor

        More text
        """
        self.coordinate = coordinate
        self.entities = entities

    @classmethod
    def new(cls,
            coordinate      :HexCoordinate):
        return cls(coordinate = coordinate,
                   entities = {})

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
        hexes = [WorldHex.new(HexCoordinate.new(0,0)),
                 WorldHex.new(HexCoordinate.new(0,1)),
                 WorldHex.new(HexCoordinate.new(1,1)),
                 WorldHex.new(HexCoordinate.new(1,0)),
                 WorldHex.new(HexCoordinate.new(0,-1)),
                 WorldHex.new(HexCoordinate.new(-1,-1)),
                 WorldHex.new(HexCoordinate.new(-1,0)),]
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




class World:
    """Container for a world

    Worlds contain all worldchunks, entities, etc.
    """

    def __init__(self,
                 name            :str,
                 uuid            :str,
                 creationDate    :str,
                 modificationDate:str,
                 current_time    :float,
                 chunks          :dict[str,WorldChunk],
                 state          : dict[str,bool]):
        """Constructor

        More text
        """
        self.name = name
        self.uuid = uuid
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.chunks = chunks
        self.current_time = current_time
        self.state = state
    
    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, 
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False)
        
    @classmethod
    def new(cls,
            name : str):
        now = datetime.datetime.now().isoformat()
        
        return cls(name                 = name,
                   uuid                 = uuid.uuid4().__str__(),
                   creationDate         = now,
                   modificationDate     = now,
                   current_time         = 0,
                   chunks               = WorldChunk.new().toDictEntry(),
                   state                = {"has wood":False})
    
    @classmethod
    def fromJSON(cls,
                 jsonfile:str|io.TextIOWrapper):
        raise NotImplementedError
    #     if isinstance(jsonfile,io.TextIOWrapper):
    #         text = jsonfile.read()
    #     else:
    #         text = jsonfile

    #     params = json.loads(text)
    #     return cls(
    #         name = params["name"],
    #         uuid = params["uuid"],
    #         creationDate = params["creationDate"],
    #         modificationDate = params["modificationDate"],
    #         current_time = params["current_time"],
    #         chunks = params["chunks"])

    def toJSON(self):
        self.modificationDate = datetime.datetime.now().isoformat()
        return self.__str__()
    
    def generateBase(self):
        base = WorldChunk.new()
        self.chunks.update({base.uuid:base})

    def addEntity(self,
                  entity:Entity,
                  coordinate:HexCoordinate):
        cell = self.findHex(coordinate)
        cell.entities.update({entity.uuid:entity})

    def findHex(self,
                coordinate:HexCoordinate) -> WorldHex: 
        for chunk in self.chunks.values():
            for cell in chunk.hexes:
                if cell.coordinate == coordinate:
                    return cell
        raise IndexError
    
    def findEntities(self,
                     entityType : Type) -> list:
        entities = []
        for chunk in self.chunks.values():
            for cell in chunk.hexes:
                for entity in cell.entities.values():
                    if isinstance(entity,entityType):
                        entities.append(entity)
        return entities
        

    def tick(self):
        mc : MainCharacter

        mc = self.findEntities(MainCharacter).pop()

        print(f"\t{self.uuid} <{type(mc)}>")
        if mc.currentAction == None and mc.actionQueue.__len__():
            mc.currentAction = mc.actionQueue.pop()

        print(f"\tAction Queue: {mc.actionQueue}")
        print(f"\tCurrent Action: {mc.currentAction}")
        if (mc.currentAction == Actions.gatherWood):
            mccell = self.findHex(mc.position)
            if any(isinstance(x,WoodPile) for x in mccell.entities.values()):
                self.state.update({"has wood":True})
                mc.currentAction = None
                return