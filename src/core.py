"""Package for running the game logic

More text
"""
import os
import io
from src.world import World
from src.mainCharacter import MainCharacter
from src.utils import HexCoordinate
from src.intelligence import PlayerIntelligence

WORLDFOLDER = "saves"

class Core:
    """Class describing the core runner of the game
    
    More text
    """

    def __init__(self):
        """Constructor

        More text
        """
        self.active = False
        return

    def activate(self):
        """Lauches the game backend systems

        More text
        """
        # wipe saves folder so it doesn't fill up with garbage
        # for file in [os.path.join(WORLDFOLDER,f) for f in os.listdir(WORLDFOLDER) if os.path.isfile(os.path.join(WORLDFOLDER,f))]:
        #     os.remove(file)

        world = World.new("bip")

        mc = MainCharacter.new()
        # mainCharacterAI = PlayerIntelligence([],mc)
        world.addEntity(mc,HexCoordinate(0,0))
        self.saveWorld(world,WORLDFOLDER)



        # with open(f"{WORLDFOLDER}/ef7c74e5-70d9-4f46-9ce9-f5f1b06adbb8.world","r") as f:
        #     world = self.loadWorld(f)
        # print(world)
        self.active = True
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