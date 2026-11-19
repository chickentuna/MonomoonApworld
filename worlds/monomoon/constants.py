from dataclasses import dataclass
from typing import List
import csv
import pkgutil


# load from csv, copied from the google sheet
stream = pkgutil.get_data(__name__, "data/pickups.csv").decode("utf-8-sig")
pickups_csv: List[List[str]] = list(csv.reader(stream.splitlines(), delimiter='\t'))

@dataclass
class RawCollectible:
    node_name: str
    ap_id: int

GAME_NAME = "MONOMOON"
MOON_PIECE_COUNT = 4
RELIC_COUNT = 8
ORB_COUNT_PER_COLOUR = 7
ORB_COLOURS = ['Red', 'Yellow', 'Blue', 'Green']
