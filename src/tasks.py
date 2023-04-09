from typing import Callable

from src.world import HexCoordinate
from src.enitity import Activity

class Task:
    condition       : Callable[[],float]
    description     : str
    location        : HexCoordinate
    action          : Activity
    tags            : list

    def __init__(self,
                 condition       : Callable[[],float],
                 location        : HexCoordinate,
                 action          : Activity,
                 tags            : list) -> None:
        self.condition = condition
        self.location = location
        self.action = action
        self.tags = tags
        pass

    def progress(self):
        return self.condition()

class SuperTask:
    tasks           : list

    def __init__(self,
                 tasks   : list):
        self.tasks = tasks

    def progress(self):
        r = [x.progress() for x in self.tasks]
        return sum(r)/len(r)
    
    def first(self) -> Task | None:
        if isinstance(self.tasks[0],SuperTask):
            return self.tasks[0].first()
        elif isinstance(self.tasks[0],Task):
            return self.tasks[0]
        else:
            return None
