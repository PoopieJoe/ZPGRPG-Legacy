"""Package for running the game logic

More text
"""
import os
import io
# import asyncio
import sched
import time
from src.world import World
from src.mainCharacter import MainCharacter
from src.enitity import WoodPile
from src.utils import HexCoordinate
from src.intelligence import GOAP

WORLDFOLDER = "saves"

TICKRATE = 1
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
        self.paused = True
        self.scheduler = sched.scheduler(time.time,time.sleep)
        return

    def activate(self):
        """Lauches the game backend systems

        More text
        """

        self.world = World.new("bip")

        mc = MainCharacter.new()
        self.world.addEntity(mc,HexCoordinate(0,0))

        woodpile_1 = WoodPile.new()
        self.world.addEntity(woodpile_1,HexCoordinate(0,0))

        self.playerIntelligence = GOAP(mc)
        self.playerIntelligence.goalstate.update({"has wood":True})
        plan = self.playerIntelligence.planner.plan(self.world.state,
                                                    self.playerIntelligence.goalstate)
        mc.actionQueue.extend(plan)
        


        ## save/reload garbo

        # wipe saves folder so it doesn't fill up with garbage
        # for file in [os.path.join(WORLDFOLDER,f) for f in os.listdir(WORLDFOLDER) if os.path.isfile(os.path.join(WORLDFOLDER,f))]:
        #     os.remove(file)
        # self.saveWorld(world,WORLDFOLDER)
        # with open(f"{WORLDFOLDER}/ef7c74e5-70d9-4f46-9ce9-f5f1b06adbb8.world","r") as f:
        #     world = self.loadWorld(f)
        # print(world)

        
        self.active = True
        self.paused = True
        self.t_prev = time.time()
        self.scheduleNextTick()
        return
    
    def saveWorld(self,
                  world:World,
                  savefolder:str):
        outputFileName = world.uuid.__str__() + ".world"
        with open(savefolder + "/" + outputFileName,"+w") as f:
            print(f"Saved world {world.name} to {outputFileName}")
            f.write(world.toJSON())
        return
    
    def loadWorld(self,
                  jsonfile:str|io.TextIOWrapper):
        return World.fromJSON(jsonfile)
    
    def tick(self,
             dt  : float):
        #update logic
        self.world.current_time = self.world.current_time + dt
        print("-----------------------------------------------------------------------------------------")
        print(f"time: {self.world.current_time},\t dt:{dt}")
        self.world.tick()
        pass
        
    def scheduleNextTick(self):
        t = time.time()
        if (not self.paused):
            self.tick(t - self.t_prev)

        if (self.scheduler.empty()):
            self.scheduler.enter(   TICKTIME - (t % TICKTIME),
                                    1,
                                    self.scheduleNextTick)
            
        self.t_prev = t
            

    def start(self):
        assert(self.active)
        self.paused = False

    def pause(self):
        self.paused = True
