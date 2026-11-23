from dataclasses import dataclass

from Options import PerGameCommonOptions, DefaultOnToggle, Choice

class Goal(Choice):
    """
    - **Fix Moon:** Collect the four moon piece items and fix the moon.
    - **The End**: Collect all emblems and complete the crown constellation.
    - **Full Moon:** Collect all relics and dragon egg orbs and birth the dragon.
    """
    display_name = "Goal"
    option_fix_moon = 0
    option_the_end = 1
    option_full_moon = 2
    
    default = 2

class RandomStartLocation(DefaultOnToggle):
    """TODO: Pick a random checkpoint as your start location if it can garantee world completion."""
    display_name = "Random Start Location"


class GateMovementMechanics(DefaultOnToggle):
    """TODO: Adds knowledge-gated movement mechanics into the pool. These include:
        - Sliding (and therefore Rolling/Diving)
        - Floating
        - Dizzy
        - Sleep
        - Frame lock
    """
    display_name = "Gate movement mechanics"

class CheckpointSanity(DefaultOnToggle):
    """TODO: Each checkpoint is a location.
    """
    display_name = "Checkpointsanity"

@dataclass
class MonomoonOptions(PerGameCommonOptions):
    goal: Goal
    random_start_location: RandomStartLocation
    gate_movement_mechanics: GateMovementMechanics
    checkpoint_sanity: CheckpointSanity