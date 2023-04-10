
from src.mainCharacter import MainCharacter
from src.utils import Action,Actions

class GOAP:
    class Planner:
        entity   : MainCharacter

        def __init__(self, 
                     entity   : MainCharacter):
            self.entity = entity
        
        def plan(self,
                 worldstate : dict[str,bool],
                 goalstate  : dict) -> list:
            diff = {}
            for key, value in worldstate.items():
                if goalstate[key] != value:
                    diff.update({key:goalstate[key]})
            print(diff)
            if diff == {}:
                print("nothing to do!")
                return []
            else:
                return [Actions.gatherWood]

    goalstate : dict[str,bool] = {}
    planner : Planner

    def __init__(self,
                 entity:MainCharacter) -> None:
        self.planner = GOAP.Planner(entity)
    