from typing import Dict

from BaseClasses import Location

from .constants import GAME_NAME, BASE_COLLECTIBLES

location_name_to_id: Dict[str, int] = BASE_COLLECTIBLES

class MonomoonLocation(Location):
    game = GAME_NAME
