from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME, pickups_csv
from .items import MonomoonItem, classification
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
        options=[OptionFilter(GateMovementMechanics,
                              GateMovementMechanics.option_true)],
        filtered_resolution=True,
    )


class MonomoonWorld(World):
    """In MONOMOON, the way forward is reserved for the knowing and the daring.
    Guided by moonlight, you’ll uncover hidden truths and wander through a tiny and mysterious open world."""

    game = GAME_NAME
    web = MonomoonWeb()
    options_dataclass = MonomoonOptions
    options: MonomoonOptions
    item_name_to_id = {}
    location_name_to_id = location_name_to_id
    origin_region_name = 'Entrance'

    def fill_slot_data(self):
        return self.options.as_dict(
            "goal",
            "random_start_location",
            "gate_movement_mechanics",
            "checkpoint_sanity",
            "moon_script_only"
        )

    def create_region(self, name) -> Region:
        region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(region)
        return region

    def create_regions(self) -> None:
        entrance = self.create_region("Entrance")
        everything = self.create_region("Everything")
        for name, loc_id in location_name_to_id.items():
            everything.locations.append(MonomoonLocation(
                self.player, name, loc_id, everything))
        entrance.connect(everything)

        # Beginnings of region based movement logic, not for v1
        '''
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
        '''

    def create_items(self) -> None:
        for row in pickups_csv:
            id, name, _ = row
            id = int(id)
            if name not in self.item_name_to_id:
                # we consider orbs as 1 item, same for moon piece
                self.item_name_to_id[name] = id
            self.multiworld.itempool.append(self.create_item(name))

    def create_item(self, name: str) -> Item:
        return MonomoonItem(name, classification(name, self.options.goal.value), self.item_name_to_id[name], self.player)

    def add_event(self, region, name, rule):
        loc = MonomoonLocation(self.player, name, None, region)
        loc.place_locked_item(MonomoonItem(
            name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)
        self.set_rule(loc, rule)

    def set_rules(self) -> None:

        # Locations only reachable with frame lock
        self.set_rule(self.get_location('Fruit Relic'), Has('Map'))
        self.set_rule(self.get_location('Mirror Relic'), Has('Map'))
        self.set_rule(self.get_location('Sea Cave Golden Quill (13,2)'), # Eye room
                      Has('Map'))

        # Sea Dragon
        self.set_rule(self.get_location('Sea Dragon', Has('Lyre')))

        # Crown Emblem Location
        self.set_rule(self.get_location('Fix Moon Reward'),
                      Has('Moon Piece', 4))

        # Endings
        goal = self.options.goal.value
        moon_region = self.get_region("Everything")  # TODO: region based logic
        shrine_region = self.get_region("Everything")
        statue_region = self.get_region("Everything")

        self.add_event(moon_region, "Fix Moon", Has("Moon Piece", 4))
        if goal > 0:
            self.add_event(shrine_region, "The End", Has("Fix Moon")
                           & Has("Sky Emblem")
                           & Has("Sea Emblem")
                           & Has("Earth Emblem")
                           & Has("Crown Emblem"))
        if goal > 1:
            self.add_event(statue_region, "Full Moon", Has("The End")
                           & Has('Skull Relic')
                           & Has('Amulet Relic')
                           & Has('Fruit Relic')
                           & Has('Mirror Relic')
                           & Has('Hourglass Relic')
                           & Has('Wand Relic')
                           & Has('Scales Relic')
                           & Has('Crown Relic')
                           & Has("Yellow Orb", 7)
                           & Has("Green Orb", 7)
                           & Has("Red Orb", 7)
                           & Has("Blue Orb", 7)
                           )

        goal_event = ["Fix Moon", "The End",
                      "Full Moon"][self.options.goal.value]
        self.set_completion_rule(Has(goal_event))
