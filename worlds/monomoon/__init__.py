from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME
from .items import MonomoonItem, item_name_to_id, classification
from .locations import MonomoonLocation, location_name_to_id, location
from .options import MonomoonOptions, GateMovementMechanics
from rule_builder.rules import Has, HasAll
from rule_builder.options import OptionFilter

class MonomoonWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "How to set up the MONOMOON randomizer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["chickentuna", "XuaTheGrate"],
    )]



def movement(*items: str):
    return HasAll(
        *items,
        options=[OptionFilter(GateMovementMechanics, GateMovementMechanics.option_true)],
        filtered_resolution=True,
    )


class MonomoonWorld(World):
    """In MONOMOON, the way forward is reserved for the knowing and the daring.
    Guided by moonlight, you’ll uncover hidden truths and wander through a tiny and mysterious open world."""

    game = GAME_NAME
    web = MonomoonWeb()
    options_dataclass = MonomoonOptions
    options: MonomoonOptions
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id


    def create_regions(self) -> None:
        entrance = Region("Entrance", self.player, self.multiworld)
        entrance.locations.append(MonomoonLocation(self.player, *location("CollectableMap"), entrance))

        west_of_entrace = Region("WestOfEntrance", self.player, self.multiworld)
        self.create_entrance(entrance, west_of_entrace, movement("Float", "Slide"))

        everything = Region("TODO", self.player, self.multiworld)
        for name, loc_id in location_name_to_id.items():
            everything.locations.append(MonomoonLocation(self.player, name, loc_id, everything))
        self.multiworld.regions.append(everything)

    def create_items(self) -> None:
        for name in item_name_to_id:
            self.multiworld.itempool.append(self.create_item(name))

    def create_item(self, name: str) -> Item:
        return MonomoonItem(name, classification(name), item_name_to_id[name], self.player)

    def set_rules(self) -> None:

        # TODO: use the RuleBuilder
        
        # TODO: completion condition
        self.multiworld.completion_condition[self.player] = lambda state: False
