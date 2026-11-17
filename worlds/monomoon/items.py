from typing import Dict

from BaseClasses import Item

from .constants import GAME_NAME

item_name_to_id: Dict[str, int] = BASE_COLLECTIBLES

class MonomoonItem(Item):
    game = GAME_NAME

def classification(name: str) -> ItemClassification:
    
    return ItemClassification.filler