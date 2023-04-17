import uuid
import src.lib as lib


class PlayerActor(lib.actors.Actor):
    def __init__(self, 
                 uuid   : str,
                 world  : lib.world.World, 
                 entity : lib.character.Character) -> None:
        super().__init__(uuid, world, entity)

    @classmethod
    def new(cls, world, entity):
        return cls(uuid     = uuid.uuid4().__str__(),
                   world    = world,
                   entity   = entity)

    def onTick(self):
        return