import uuid

import src.lib as lib

class WoodPile(lib.entity.Immutable):
    inventory : lib.item.Inventory

    def __init__(self,
                 uuid           : str,
                 properties     : list,
                 position       : lib.utils.Point,
                 inventory      : lib.item.Inventory):
        lib.entity.Immutable.__init__(self,
                        uuid,
                        properties,
                        position)
        self.inventory = inventory

    @classmethod
    def new(cls,
            position    : lib.utils.Point):
        return cls(uuid         = uuid.uuid4().__str__(),
                   properties   = ["is_wood"],
                   position     = position,
                   inventory    = lib.item.Inventory())