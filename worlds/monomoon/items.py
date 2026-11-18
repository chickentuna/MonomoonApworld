from typing import Dict

from BaseClasses import Item, ItemClassification
from .constants import GAME_NAME, BASE_COLLECTIBLES

item_name_to_id: Dict[str, int] = {}
for raw in BASE_COLLECTIBLES:
    item_name_to_id[raw.node_name] = raw.ap_id
item_name_to_id['Relic'] = 5000
item_name_to_id['Moon Piece'] = 6000
item_name_to_id['Sky Emblem'] = 7002

class MonomoonItem(Item):
    game = GAME_NAME

def classification(name: str) -> ItemClassification:
    # TODO: to decide based on the run's goal. Consider gems, relics, moon pieces.
    PROGRESSIVE_COLLECTIBLES = [
        'CollectableMap',
        'CollectableInstrument',
        'CollectableMarkers',
        'CollectablePageCD', # Womb puzzle chest page
        'CollectablePageCRS', # Repel stone chest page
        'CollectablePageCRB', # Ritual bed chest page
        'CollectablePageCDW', # Diamonds wall chest page
    ]
    
    if name in PROGRESSIVE_COLLECTIBLES or 'CollectableOrb' in name:
        return ItemClassification.progression
    if 'Relic' in name:
        return ItemClassification.progression
    if 'Emblem' in name:
        return ItemClassification.progression
    if name == 'Moon Piece':
        return ItemClassification.progression
    return ItemClassification.useful