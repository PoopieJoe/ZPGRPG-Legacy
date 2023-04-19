import uuid
import enum
import src.lib as lib


class PlayerActor(lib.Actor,lib.FSM):
    class States(lib.FSM.FSMStates):
        idle = enum.auto(),
        moveTo = enum.auto(),
        performAction = enum.auto()

    def __init__(self, 
                 uuid   : str,
                 world  : lib.World, 
                 entity : lib.Character) -> None:
        super().__init__(uuid, world, entity)
        self.state = PlayerActor.States.idle

    target          : lib.Entity | lib.Vector3D | None
    facingDirection : lib.Vector3D

    def updateFSM(self):
        if self.state == PlayerActor.States.idle:
            pass
        elif self.state == PlayerActor.States.moveTo:
            pass
        elif self.state == PlayerActor.States.performAction:
            pass
            

    @classmethod
    def new(cls, world, entity):
        return cls(uuid     = uuid.uuid4().__str__(),
                   world    = world,
                   entity   = entity)

    def onTick(self,
               dt   : float):
        if self.state == PlayerActor.States.moveTo:
            self.entity.transpose(self.facingDirection * self.entity.speed * dt)
        