"""Package for running the game logic

More text
"""
import os
import io
# import asyncio
import sched
import time

from src.worldActors.playerActor import PlayerActor
import src.lib as lib

from src.worldObjects.resources import WoodPile
from src.ai.goap import GOAP

WORLDFOLDER = "saves"

TICKRATE = 128
TICKTIME = 1/TICKRATE

class Core:
    """Class describing the core runner of the game
    
    More text
    """

    def __init__(self):
        """Constructor

        More text
        """
        self.active = False
        self._paused = True
        self._scheduler = sched.scheduler(time.time,time.sleep)
        return

    def activate(self):
        """Lauches the game backend systems

        More text
        """

        self.world = lib.world.World.new("bip")
        newchar = lib.character.Character.new((0,0,0))
        newchar.speed = 10
        self.world.addEntity(newchar)
        newactor = PlayerActor.new(self.world,newchar)
        newactor.facingDirection = lib.utils.Vector3D(1,0,0)
        newactor.state = PlayerActor.States.moveTo
        self.world.addActor(newactor)

        


        ## save/reload garbo

        # wipe saves folder so it doesn't fill up with garbage
        # for file in [os.path.join(WORLDFOLDER,f) for f in os.listdir(WORLDFOLDER) if os.path.isfile(os.path.join(WORLDFOLDER,f))]:
        #     os.remove(file)
        # self.saveWorld(world,WORLDFOLDER)
        # with open(f"{WORLDFOLDER}/ef7c74e5-70d9-4f46-9ce9-f5f1b06adbb8.world","r") as f:
        #     world = self.loadWorld(f)
        # print(world)

        
        self.active = True
        self._paused = True
        self.t_prev = time.time()
        self.scheduleNextTick()
        return
    
    @property
    def paused(self):
        return self._paused
    
    def start(self):
        assert(self.active)
        self._paused = False

    def pause(self):
        self._paused = True

    def run(self):
        self._scheduler.run()

    def saveWorld(self,
                  world:lib.world.World,
                  savefolder:str):
        outputFileName = world.uuid.__str__() + ".world"
        with open(savefolder + "/" + outputFileName,"+w") as f:
            print(f"Saved world {world.name} to {outputFileName}")
            f.write(world.toJSON())
        return
    
    def loadWorld(self,
                  jsonfile:str|io.TextIOWrapper):
        return lib.world.World.fromJSON(jsonfile)
    
    def tick(self,
             dt  : float):
        #update logic
        self.world.current_time = self.world.current_time + dt
        print("-----------------------------------------------------------------------------------------")
        print(f"time: {self.world.current_time},\t dt:{dt}")
        print(f"Entities: {self.world.findEntities(lib.character.Character)[0].position}")
        self.world.tick(dt)
        pass
        
    def scheduleNextTick(self):
        t = time.time()
        if (not self._paused):
            self.tick(t - self.t_prev)

        if (self._scheduler.empty()):
            self._scheduler.enter(   TICKTIME - (t % TICKTIME),
                                    1,
                                    self.scheduleNextTick)
            
        self.t_prev = t
            

