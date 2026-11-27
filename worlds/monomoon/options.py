from dataclasses import dataclass

from Options import PerGameCommonOptions, DefaultOnToggle, Choice, Toggle, Visibility

class Goal(Choice):
    """
    - **Fix Moon:** Collect the four moon fragment items and fix the moon.
    - **The End**: Collect all emblems and complete the crown constellation.
    - **Full Moon:** Collect all relics and dragon egg orbs and birth the dragon.
    """
    display_name = "Goal"
    option_fix_moon = 0
    option_the_end = 1
    option_full_moon = 2
    
    default = 0

class RandomStartLocation(DefaultOnToggle):
    """TODO: Pick a random checkpoint as your start location if it can garantee world completion."""
    display_name = "Random Start Location"
    visibility = Visibility.none

class RandomStartLocation(DefaultOnToggle):
    """TODO: Pick a random checkpoint as your start location if it can garantee world completion."""
    display_name = "Random Start Location"
    visibility = Visibility.none

class GateMovementMechanics(DefaultOnToggle):
    """TODO: Adds knowledge-gated movement mechanics into the pool. These include:
        - Sliding (and therefore Rolling/Diving)
        - Floating
        - Dizzy
        - Sleep
        - Frame lock
    """
    display_name = "Gate movement mechanics"
    visibility = Visibility.none

class CheckpointSanity(Toggle):
    """TODO: Each checkpoint is a location.
    """
    display_name = "Checkpointsanity"
    visibility = Visibility.none

class MoonScriptOnly(Toggle):
    """Archipelago popups are all written in the game's alphabet. Non-alpha falls back on regular font.
    """
    display_name = "Moon script only"

class StartWithMap(DefaultOnToggle):
    """ Removes the map item from the pool so you can fast travel from the start
    """
    display_name = "Start with map"

@dataclass
class MonomoonOptions(PerGameCommonOptions):
    goal: Goal
    moon_script_only: MoonScriptOnly
    start_with_map: StartWithMap
    random_start_location: RandomStartLocation
    gate_movement_mechanics: GateMovementMechanics
    checkpoint_sanity: CheckpointSanity