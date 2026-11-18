from typing import Dict, Tuple

from BaseClasses import Location

from .constants import GAME_NAME, BASE_COLLECTIBLES

location_name_to_id: Dict[str, int] = {}
for raw in BASE_COLLECTIBLES:
    location_name_to_id[raw.node_name] = raw.ap_id
class MonomoonLocation(Location):
    game = GAME_NAME

def location(name: str) -> Tuple[str, int]:
    return (name, location_name_to_id[name])
