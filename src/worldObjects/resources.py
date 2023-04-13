import uuid

import src.lib as lib

class WoodPile(lib.entity.Immovable):
    inventory : lib.item.Inventory

    def __init__(self,
                 uuid           : str,
                 properties     : list,
                 position       : lib.utils.HexCoordinate,
                 inventory      : lib.item.Inventory):
        lib.entity.Immovable.__init__(self,
                        uuid,
                        properties,
                        position)
        self.inventory = inventory

    @classmethod
    def new(cls):
        return cls(uuid         = uuid.uuid4().__str__(),
                   properties   = ["is_wood"],
                   position     = lib.utils.HexCoordinate(0,0),
                   inventory    = lib.item.Inventory())