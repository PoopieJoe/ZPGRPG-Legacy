"""world package

more text
"""
from __future__ import annotations
import io
import json
import datetime
import uuid

from typing import Type,TypeVar,Any
import src.lib as lib

WORLDFOLDER = "../../saves"

# TODO move to higher layer?
class World:
    """Container for a world

    Worlds contain all worldchunks, entities, etc.
    """

    def __init__(self,
                 name               : str,
                 uuid               : str,
                 creationDate       : str,
                 modificationDate   : str,
                 current_time       : float,
                 chunks             : dict[str,lib.map.WorldChunk],
                 entities           : dict[str,lib.entity.Entity],
                 actors             : dict[str,lib.actors.Actor],
                 state              : dict[str,bool]):
        """Constructor

        More text
        """
        self.name = name
        self.uuid = uuid
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.chunks = chunks
        self.current_time = current_time
        self.entities = entities
        self.actors = actors
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
                   chunks               = lib.map.WorldChunk.new().toDictEntry(),
                   entities             = {},
                   actors               = {},
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
        base = lib.map.WorldChunk.new()
        self.chunks.update({base.uuid:base})


    def loadChunk(self,src):
        # load chunk from src
        raise NotImplementedError

    def addEntity(self,
                  entity        : lib.entity.Entity,
                  coordinate    : lib.utils.HexCoordinate | None = None):
        if coordinate:
            entity.position = coordinate
        self.entities.update(entity.toDict())

    def addActor(self,
                 actor          : lib.actors.Actor):
        self.actors.update
        

    def findHex(self,
                coordinate:lib.utils.HexCoordinate) -> lib.map.WorldHex: 
        for chunk in self.chunks.values():
            for cell in chunk.hexes:
                if cell.coordinate == coordinate:
                    return cell
        raise IndexError
    
    TEntity = TypeVar("TEntity", bound=lib.entity.Entity)

    def findEntities(self,
                     entityType : Type[TEntity]) -> list[TEntity]:
        e = []
        for entity in self.entities.values():
            if isinstance(entity,type(entityType)):
                e.append(entity)
        return e
    
    def findClosest(self,
                    sourceEntity : lib.entity.Entity,
                    entityType : Type[TEntity]) -> TEntity | None:
        foundEntities = self.findEntities(entityType)

        closest = None
        for entity in foundEntities:
            if closest == None:
                closest = entity
            elif entity.position.distanceFrom(sourceEntity.position) < closest.position.distanceFrom(sourceEntity.position):
                closest = entity

        return closest
        

    def tick(self):
        pass

