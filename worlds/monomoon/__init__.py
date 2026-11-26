from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME, pickups_csv
from .items import MonomoonItem, classification, item_name_to_id
from .locations import MonomoonLocation, location_name_to_id
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
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    origin_region_name = 'Entrance'

    def fill_slot_data(self):
        return self.options.as_dict(
            "goal",
            # "random_start_location",
            # "gate_movement_mechanics",
            # "checkpoint_sanity",
            "moon_script_only",
            "start_with_map"
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

    def create_items(self) -> None:
        for row in pickups_csv:
            _, name, _ = row
            if name == "Map" and self.options.start_with_map.value:
                self.multiworld.push_precollected(self.create_item(name))
            else:
                self.multiworld.itempool.append(self.create_item(name))

        my_item_count = len([_ for item in self.multiworld.itempool if item.player == self.player])
        my_location_count = len(self.multiworld.get_unfilled_locations(self.player))
        self.multiworld.itempool += [self.create_filler() for _ in range(my_location_count - my_item_count)]

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_item(self, name: str) -> Item:
        return MonomoonItem(name, classification(name, self.options.goal.value), self.item_name_to_id[name], self.player)

    def add_event(self, region, name, rule):
        loc = MonomoonLocation(self.player, name, None, region)
        loc.place_locked_item(MonomoonItem(
            name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)
        self.set_rule(loc, rule)

    def set_rules(self) -> None:

        self.set_rule(self.get_location('Fruit Relic'), Has('Map'))
        self.set_rule(self.get_location('Mirror Relic'), HasAll('Map', 'Lyre', 'Map Markers', 'Map'))
        self.set_rule(self.get_location('Sea Dragon'), Has('Lyre'))
        self.set_rule(self.get_location('Castle Golden Quill'), HasAll('Lyre', 'Map Markers', 'Map'))
        self.set_rule(self.get_location('Swamp Quill (3,9)'), Has('Lyre'))
        self.set_rule(self.get_location('Swamp Blue Orb (4,11)'), HasAll('Lyre', 'Map Markers', 'Map'))
        self.set_rule(self.get_location('Sea Cave Red Orb (7,3)'), Has('Lyre'))
        
        # Eye room
        self.set_rule(self.get_location('Sea Cave Golden Quill (13,2)'), HasAll('Lyre', 'Map', 'Map Markers'))

        # Beyond City Entrance
        self.set_rule(self.get_location('City Quill (27,9)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Cavern Green Orb (28,12)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Rabbit Telescope'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Hourglass Relic'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('City Red Orb (28,5)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('City Quill (27,3)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('City Red Orb (24,6)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Catacombs Green Orb (23,7)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('City Quill (23,6)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Conch'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Abyss Red Orb (17,2)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Abyss Golden Quill (14,2)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Catacombs Quill (25,8)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Den Green Orb (23,13)'), HasAll('Map Markers', 'Map'))
        self.set_rule(self.get_location('Skull Relic'), HasAll('Map Markers', 'Map'))

        # Beyond roof (need lyre for cube or map markers for torches)
        self.set_rule(self.get_location('Glade Yellow Orb (16,17)'), HasAll('Map Markers', 'Map') | Has('Lyre'))

        # Endings
        goal = self.options.goal.value
        moon_region = self.get_region("Everything")  # TODO: region based logic
        shrine_region = self.get_region("Everything")
        statue_region = self.get_region("Everything")

        self.add_event(moon_region, "Fix Moon", Has("Moon Piece", 4) & (HasAll('Map Markers', 'Map') | Has('Lyre')))
        
        # Scales Relic
        self.set_rule(self.get_location('Scales Relic'), HasAll('Map Markers', 'Map', 'Fix Moon'))
        # Crown Emblem
        self.set_rule(self.get_location('Fix Moon Reward'), Has('Fix Moon'))

        if goal > 0:
            self.add_event(shrine_region, "The End", HasAll(
                    "Fix Moon",
                    "Sky Emblem",
                    "Sea Emblem",
                    "Earth Emblem",
                    "Crown Emblem",
                    "Lyre",
                    "Map Markers",
                    "Map",
                    "Page: Chest Two-Button Door",
                    "Page: Chest Repel Stone",
                    "Page: Chest Diamonds Wall",
                    "Page: Chest Ritual Bed",
                )
            )
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
                           & Has("Map")
                           & Has("Map Markers")
                           )

        goal_event = ["Fix Moon", "The End", "Full Moon"][self.options.goal.value]
        self.set_completion_rule(Has(goal_event))
