from abc import ABC,abstractmethod
from typing import Type,TypeVar,Any

class Item:
    @property
    @abstractmethod
    def tags(self) -> list[str]:
        pass

class Wood(Item):
    @property
    def tags(self) -> list[str]:
        return ["Flammable"]

class Inventory:
    contents : list[Item] = []

    TItem = TypeVar("TItem",bound=Item)
    def contains(self,
                 itemType : Type[TItem]) -> bool:
        for item in self.contents:
            if type(item) == itemType:
                return True
        return False