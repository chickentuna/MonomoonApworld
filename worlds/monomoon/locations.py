from typing import Dict, Tuple

from BaseClasses import Location

from .constants import GAME_NAME, pickups_csv

location_name_to_id: Dict[str, int] = {}

for row in pickups_csv:
    id, _, loc_name = row
    id = int(id)
    location_name_to_id[loc_name] = id


class MonomoonLocation(Location):
    game = GAME_NAME

def location(name: str) -> Tuple[str, int]:
    return (name, location_name_to_id[name])
