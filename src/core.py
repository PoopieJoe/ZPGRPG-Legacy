"""Package for running the game logic

More text
"""
import os
import io
from src.world import World
from src.mainCharacter import MainCharacter
from src.utils import HexCoordinate

WORLDFOLDER = "saves"

class Core:
    """Class describing the core runner of the game
    
    More text
    """

    def __init__(
        self
    ):
        """Constructor

        More text
        """
        self.active = False
        return

    def activate(
        self
    ):
        """Lauches the game backend systems

        More text
        """
        # wipe saves folder so it doesn't fill up with garbage
        for file in [os.path.join(WORLDFOLDER,f) for f in os.listdir(WORLDFOLDER) if os.path.isfile(os.path.join(WORLDFOLDER,f))]:
            os.remove(file)

        world = World.new("bip")

        mc = MainCharacter.new()
        world.addEntity(mc,HexCoordinate(0,0))
        self.saveWorld(world,WORLDFOLDER)



        # with open("saves/a0de3700-006e-48e4-bd0f-269413afb7a1.world","r") as f:
        #     world = self.loadWorld(f)
        print(world)
        self.active = True
        return
    
    def saveWorld(
        self,
        world:World,
        savefolder:str
    ):
        with open(savefolder + "/" + world.uuid.__str__() + ".world","+w") as f:
            f.write(world.toJSON())
        return
    
    def loadWorld(
        self,
        jsonfile:str|io.TextIOWrapper
    ):
        return World.fromJSON(jsonfile)