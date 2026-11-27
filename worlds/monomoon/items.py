from typing import Dict

from BaseClasses import Item, ItemClassification
from .constants import GAME_NAME, ORB_COLOURS, pickups_csv

FILLER_NAME = "Nothing"

item_name_to_id: Dict[str, int] = {
    FILLER_NAME: 1
}
for row in pickups_csv:
    id, name, _ = row
    id = int(id)
    if name not in item_name_to_id:
        # we consider orbs as 1 item, same for moon fragment, so we keep the first id in the list
        item_name_to_id[name] = id

class MonomoonItem(Item):
    game = GAME_NAME

def classification(name: str, goal_value:int) -> ItemClassification:
    for_the_end = ItemClassification.progression if goal_value > 0 else ItemClassification.filler
    for_full_moon = ItemClassification.progression if goal_value > 1 else ItemClassification.filler

    
    if name in ['Page: Castle Power Mechanism', 'Moon Fragment']:
        return ItemClassification.progression
    if 'Page: Chest' in name:
        return for_the_end
    if name.endswith('Relic'):
        return for_full_moon
    if 'Emblem' in name:
        return for_the_end
    for col in ORB_COLOURS:
        if name.startswith(f'{col} Orb'):
            return for_full_moon
    if name in ['Lyre', 'Map', 'Map Markers']:
        return ItemClassification.progression | ItemClassification.useful
    if name in ['Conch']:
        return ItemClassification.useful

    return ItemClassification.filler

item_name_groups = {
    "Orbs": ["Yellow Orb", "Red Orb", 'Blue Orb', 'Green Orb'],
    "Pages": [name for name in item_name_to_id if name.startswith('Page: ')],
    "Relics": [name for name in item_name_to_id if not name.startswith('Page: ') and name.endswith('Relic')],
    "Emblems": [name for name in item_name_to_id if not name.startswith('Page: ') and name.endswith('Emblem')]
}