from dataclasses import dataclass
from typing import List


@dataclass
class RawCollectible:
    node_name: str
    ap_id: int

GAME_NAME = "MONOMOON"

# NOTE: These are temporary names that correspond to the game's Node names of the collectibles.
# We will map them to human readable names. And we will also separate location ids and item ids into separate dictionaries.
BASE_COLLECTIBLES: List[RawCollectible] = [
    RawCollectible('CollectableMap', 1000),
    RawCollectible('CollectableConch', 1001),
    RawCollectible('CollectableInstrument', 1002),
    RawCollectible('CollectableMarkers', 1003),
    RawCollectible('CollectablePageRS', 2000),
    RawCollectible('CollectablePageMM', 2001),
    RawCollectible('CollectablePageCU', 2002),
    RawCollectible('CollectablePageC', 2003),
    RawCollectible('CollectablePageCI', 2004),
    RawCollectible('CollectablePageCPM', 2005),
    RawCollectible('CollectablePageSDMG', 2006),
    RawCollectible('CollectablePageCO', 2007),
    RawCollectible('CollectablePageDC', 2008),
    RawCollectible('CollectablePageMG', 2009),
    RawCollectible('CollectablePageEDMG', 2010),
    RawCollectible('CollectablePageCRB', 2011),
    RawCollectible('CollectablePageS', 2012),
    RawCollectible('CollectablePageT', 2013),
    RawCollectible('CollectablePageCR', 2014),
    RawCollectible('CollectablePageWWWW', 2015),
    RawCollectible('CollectablePageWM', 2016),
    RawCollectible('CollectablePageCM', 2017),
    RawCollectible('CollectablePageET', 2018),
    RawCollectible('CollectablePageSC', 2019),
    RawCollectible('CollectablePageWDMG', 2020),
    RawCollectible('CollectablePageWDPH', 2021),
    RawCollectible('CollectablePageSDPH', 2022),
    RawCollectible('CollectablePageCD', 2023),
    RawCollectible('CollectablePageCRS', 2024),
    RawCollectible('CollectablePageCDW', 2025),
    RawCollectible('CollectablePageE', 2026),
    RawCollectible('CollectablePageR', 2027),
    RawCollectible('CollectableOrb', 3000),
    RawCollectible('CollectableOrb2', 3001),
    RawCollectible('CollectableOrb3', 3002),
    RawCollectible('CollectableOrb4', 3003),
    RawCollectible('CollectableOrb5', 3004),
    RawCollectible('CollectableOrb6', 3005),
    RawCollectible('CollectableOrb7', 3006),
    RawCollectible('CollectableOrb8', 3007),
    RawCollectible('CollectableOrb9', 3008),
    RawCollectible('CollectableOrb10', 3009),
    RawCollectible('CollectableOrb11', 3010),
    RawCollectible('CollectableOrb12', 3011),
    RawCollectible('CollectableOrb13', 3012),
    RawCollectible('CollectableOrb14', 3013),
    RawCollectible('CollectableOrb15', 3014),
    RawCollectible('CollectableOrb16', 3015),
    RawCollectible('CollectableOrb17', 3016),
    RawCollectible('CollectableOrb18', 3017),
    RawCollectible('CollectableOrb19', 3018),
    RawCollectible('CollectableOrb20', 3019),
    RawCollectible('CollectableOrb21', 3020),
    RawCollectible('CollectableOrb22', 3021),
    RawCollectible('CollectableOrb23', 3022),
    RawCollectible('CollectableOrb24', 3023),
    RawCollectible('CollectableOrb25', 3024),
    RawCollectible('CollectableOrb26', 3025),
    RawCollectible('CollectableOrb27', 3026),
    RawCollectible('CollectableOrb28', 3027),
    RawCollectible('CollectableGoldenQuill3', 4000),
    RawCollectible('CollectableGoldenQuill2', 4001),
    RawCollectible('CollectableGoldenQuill', 4002),
    RawCollectible('CollectableGoldenQuill4', 4003),
    RawCollectible('CollectableGoldenQuill5', 4004)
]
# TODO: include relics, gems, moon pieces.


MOON_PIECE_COUNT = 4
RELIC_COUNT = 8
ORB_COUNT_PER_COLOUR = 7