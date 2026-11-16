from typing import Dict
from dataclasses import dataclass
from BaseClasses import ItemClassification


@dataclass
class RawCollectible:
    node_name: str
    ap_id: int
    classification: ItemClassification

GAME_NAME = "MONOMOON"

# NOTE: These are temporary names that correspond to the game's Node names of the collectibles.
# We will map them to human readable names. And we will also separate location ids and item ids into separate dictionaries.

BASE_COLLECTIBLES_TEMP: Dict[str, int] = {
    'CollectableMap': 1000
    'CollectableConch': 1001,
    'CollectableInstrument': 1002,
    'CollectableMarkers': 1003,
    'CollectablePageRS': 2000,
    'CollectablePageMM': 2001,
    'CollectablePageCU': 2002,
    'CollectablePageC': 2003,
    'CollectablePageCI': 2004,
    'CollectablePageCPM': 2005,
    'CollectablePageSDMG': 2006,
    'CollectablePageCO': 2007,
    'CollectablePageDC': 2008,
    'CollectablePageMG': 2009,
    'CollectablePageEDMG': 2010,
    'CollectablePageCRB': 2011,
    'CollectablePageS': 2012,
    'CollectablePageT': 2013,
    'CollectablePageCR': 2014,
    'CollectablePageWWWW': 2015,
    'CollectablePageWM': 2016,
    'CollectablePageCM': 2017,
    'CollectablePageET': 2018,
    'CollectablePageSC': 2019,
    'CollectablePageWDMG': 2020,
    'CollectablePageWDPH': 2021,
    'CollectablePageSDPH': 2022,
    'CollectablePageCD': 2023,
    'CollectablePageCRS': 2024,
    'CollectablePageCDW': 2025,
    'CollectablePageE': 2026,
    'CollectablePageR': 2027,
    'CollectableOrb': 3000,
    'CollectableOrb2': 3001,
    'CollectableOrb3': 3002,
    'CollectableOrb4': 3003,
    'CollectableOrb5': 3004,
    'CollectableOrb6': 3005,
    'CollectableOrb7': 3006,
    'CollectableOrb8': 3007,
    'CollectableOrb9': 3008,
    'CollectableOrb10': 3009,
    'CollectableOrb11': 3010,
    'CollectableOrb12': 3011,
    'CollectableOrb13': 3012,
    'CollectableOrb14': 3013,
    'CollectableOrb15': 3014,
    'CollectableOrb16': 3015,
    'CollectableOrb17': 3016,
    'CollectableOrb18': 3017,
    'CollectableOrb19': 3018,
    'CollectableOrb20': 3019,
    'CollectableOrb21': 3020,
    'CollectableOrb22': 3021,
    'CollectableOrb23': 3022,
    'CollectableOrb24': 3023,
    'CollectableOrb25': 3024,
    'CollectableOrb26': 3025,
    'CollectableOrb27': 3026,
    'CollectableOrb28': 3027,
    'CollectableGoldenQuill3': 4000,
    'CollectableGoldenQuill2': 4001,
    'CollectableGoldenQuill': 4002,
    'CollectableGoldenQuill4': 4003,
    'CollectableGoldenQuill5': 4004,
    'CollectableTrophy': 5000,
    'CollectableTrophyAmulet': 5001,
    'CollectableTrophyFruit': 5002,
    'CollectableTrophyMirror': 5003,
    'CollectableTrophyHourglass': 5004,
    'CollectableTrophyWand': 5005,
    'CollectableTrophy': 5006,
    'CollectableTrophy': 5007,
    'OwlTelescope': 6000,
    'RabbitTelescope2': 6001,
    'FishTelescope3': 6002,
    'BigTelescope': 6003,
}

BASE_COLLECTIBLES: List[RawCollectible] = [

]