from typing import Dict

from BaseClasses import Location

from .constants import GAME_NAME, BASE_COLLECTIBLES

# NOTE: These are temporary names that correspond to the game's Node names of the collectibles.
# We will map them to human readable names.
location_name_to_id: Dict[str, int] = BASE_COLLECTIBLES


class MonomoonLocation(Location):
    game = GAME_NAME
