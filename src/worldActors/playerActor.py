
import src.lib as lib


class PlayerActor(lib.actors.Actor):
    def __init__(self, 
                 world: lib.world.World, 
                 entity: lib.character.Character) -> None:
        super().__init__(world, entity)

    def onTick(self):
        return