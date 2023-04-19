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
                 chunks             : dict[str,lib.WorldChunk],
                 entities           : dict[str,lib.Entity],
                 actors             : dict[str,lib.Actor],
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
                   chunks               = lib.map.WorldChunk.new((0,0,0)).toDictEntry(),
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
        base = lib.WorldChunk.new((0,0,0))
        self.chunks.update({base.uuid:base})


    def loadChunk(self,src):
        # load chunk from src
        raise NotImplementedError

    def addEntity(self,
                  entity        : lib.Entity,
                  coordinate    : lib.Vector3D | None = None):
        if coordinate:
            entity.position = coordinate
        self.entities.update(entity.toDict())

    def removeEntity(self,
                     entity     : lib.Entity | str,):
        if isinstance(entity,lib.Entity):
            self.entities.pop(entity.uuid)
        else:
            self.entities.pop(entity)
        

    def addActor(self,
                 actor          : lib.Actor):
        if actor.entity.uuid not in self.entities:
            raise ValueError("Associated entitiy not in world")
        self.actors.update(actor.toDict())
        

    def findChunk(  self,
                    coordinate      : lib.Vector3D,
                    createOnError   : bool = False) -> lib.WorldChunk: 
        for chunk in self.chunks.values():
            if chunk.inChunk(coordinate):
                return chunk
        if not createOnError:
            raise IndexError
        return lib.WorldChunk.new(lib.Vector3D( int(coordinate.x/lib.CHUNKSIZE), int(coordinate.y/lib.CHUNKSIZE), int(coordinate.z/lib.CHUNKSIZE)))
    
    TEntity = TypeVar("TEntity", bound=lib.entity.Entity)

    def findEntities(self,
                     entityType : Type[TEntity]) -> list[TEntity]:
        e = []
        for entity in self.entities.values():
            if type(entity) == entityType:
                e.append(entity)
        return e
    
    def findClosest(self,
                    sourceEntity : lib.Entity,
                    entityType : Type[TEntity]) -> TEntity | None:
        foundEntities = self.findEntities(entityType)

        closest = None
        for entity in foundEntities:
            if closest == None:
                closest = entity
            elif entity.position.distanceFrom(sourceEntity.position) < closest.position.distanceFrom(sourceEntity.position):
                closest = entity

        return closest
        

    def tick(self,
             dt : float):
        for actor in self.actors.values():
            actor.onTick(dt)
        pass

