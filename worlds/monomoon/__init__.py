from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME, MOON_PIECE_COUNT, ORB_COUNT_PER_COLOUR, RELIC_COUNT
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
    origin_region_name = 'Entrance'


    def create_regions(self) -> None:
        entrance = Region("Entrance", self.player, self.multiworld)
        self.multiworld.regions.append(entrance)
        entrance.locations.append(MonomoonLocation(self.player, *location("CollectableMap"), entrance))

        west_of_entrace = Region("WestOfEntrance", self.player, self.multiworld)
        self.multiworld.regions.append(west_of_entrace)
        self.create_entrance(entrance, west_of_entrace, movement("Float", "Slide"))

        everything = Region("TODO", self.player, self.multiworld)
        for name, loc_id in location_name_to_id.items():
            if name == 'CollectableMap':
                # used in test above so can't go in todo bin
                continue
            everything.locations.append(MonomoonLocation(self.player, name, loc_id, everything))
        self.multiworld.regions.append(everything)

        entrance.connect(everything)

    def create_items(self) -> None:
        for name in item_name_to_id:
            self.multiworld.itempool.append(self.create_item(name))
        for _ in range(MOON_PIECE_COUNT):
            self.multiworld.itempool.append(self.create_item('Moon Piece'))
        for _ in range(RELIC_COUNT):
            self.multiworld.itempool.append(self.create_item('Relic'))
        for _ in range(ORB_COUNT_PER_COLOUR):
            for col in ['Red', 'Yellow', 'Blue', 'Green']:
                self.multiworld.itempool.append(self.create_item(f'{col} Orb'))


    def create_item(self, name: str) -> Item:
        return MonomoonItem(name, classification(name), item_name_to_id[name], self.player)

    def add_event(self, region, name, rule):
        loc = MonomoonLocation(self.player, name, None, region)
        loc.place_locked_item(MonomoonItem(name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)
        self.set_rule(loc, rule)

    def set_rules(self) -> None:

        # Endings
        moon_region = self.get_region("TODO")
        shrine_region = self.get_region("TODO")
        statue_region = self.get_region("TODO")
        # NOTE: temporary names for testing out logic
        self.add_event(moon_region, "Fix Moon", Has("Moon Piece", 4))
        self.add_event(shrine_region, "The End", Has("Fix Moon") & Has("Sky Emblem"))
        self.add_event(statue_region, "Full Moon", Has("The End") 
                       & Has("Relic", 8) 
                       & Has("Yellow Orb", 7)
                       & Has("Green Orb", 7)
                       & Has("Red Orb", 7)
                       & Has("Blue Orb", 7)
                       )

        goal_event = ["Fix Moon", "The End", "Full Moon"][self.options.goal.value]
        self.set_completion_rule(Has(goal_event))
