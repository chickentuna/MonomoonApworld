from dataclasses import dataclass

from Options import PerGameCommonOptions, DefaultOnToggle, Choice

class Goal(Choice):
    """TODO.

    - **Fix Moon:** Collect the four moon piece items and fix the moon.
    - **The End**: Collect all Gems and obtain the crown relic.
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


@dataclass
class MonomoonOptions(PerGameCommonOptions):
    goal: Goal = Goal()
    random_start_location: RandomStartLocation = RandomStartLocation()