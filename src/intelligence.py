from src.tasks import SuperTask,Task
from src.mainCharacter import MainCharacter

class PlayerIntelligence(SuperTask):
    mainCharacter   : MainCharacter
    tasks           : list[Task|SuperTask]

    def __init__(self, 
                 tasks          : list[Task|SuperTask],
                 mainCharacter  : MainCharacter):
        super().__init__(tasks)
        self.mainCharacter = mainCharacter

    def nextTask(self):
        ## sort task list
        pass
        
    def taskExecute(self):
        task = self.first()
        if task == None:
            return
        if task.location != self.mainCharacter.position:
            print("Moving to new location")
            