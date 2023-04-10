import uuid
import json
from typing import Type
from src.enitity import Entity,Activity
from src.utils import HexCoordinate
from src.utils import Action,Actions

class MainCharacter(Entity):
    def __init__(self,
                 uuid           : str,
                 position       : HexCoordinate,
                 activity       : Activity,
                 properties     : list,
                 actions        : list,
                 actionQueue    : list[Action],
                 currentAction  : Action | None
                 ):
        """Constructor

        More text
        """
        Entity.__init__(self,uuid,properties)
        self.position = position
        self.activity = activity
        self.actions = actions
        self.actionQueue = actionQueue
        self.currentAction = currentAction
        return
    
    # def __str__(self):
    #     return json.dumps(self,
    #                       default=lambda o: o.__dict__, 
    #                       sort_keys=True,
    #                       indent=4,
    #                       ensure_ascii=False)
    
    @classmethod
    def new(cls):
        return cls(uuid            = uuid.uuid4().__str__(),
                position        = HexCoordinate.new(0,0),
                activity        = Activity.idle,
                properties      = [],
                actions         = [Actions.goto,Actions.gatherWood],
                actionQueue     = [],
                currentAction   = None)
    
    

    # @classmethod
    # def fromJSON(cls,
    #              jsonText:str):
    #     params = json.loads(jsonText)
    #     return cls(uuid         = params["uuid"],
    #                position     = params["position"],
    #                activity     = params["activity"],
    #                properties   = params["properties"])

    # def toJSON(self):
    #     return self.__str__()