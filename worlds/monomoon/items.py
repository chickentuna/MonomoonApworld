from typing import Dict

from BaseClasses import Item, ItemClassification
from .constants import GAME_NAME, ORB_COLOURS


class MonomoonItem(Item):
    game = GAME_NAME

def classification(name: str, goal_value:int) -> ItemClassification:
    for_the_end = ItemClassification.progression if goal_value > 0 else ItemClassification.filler
    for_full_moon = ItemClassification.progression if goal_value > 1 else ItemClassification.filler

    if name.startswith('Moon Piece'):
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
    if name in ['Lyre', 'Map']:
        return ItemClassification.progression | ItemClassification.useful
    if name in ['Conch']:
        return ItemClassification.useful
    if name == 'Map Markers':
        return ItemClassification.progression

    
    return ItemClassification.filler