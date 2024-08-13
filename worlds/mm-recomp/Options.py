from typing import Dict

from Options import Choice, Option, Toggle, StartInventoryPool


#class HardMode(Toggle):
#    """Only for the most masochistically inclined... Requires button activation!"""
#    display_name = "Hard Mode"


#class ButtonColor(Choice):
#    """Customize your button! Now available in 12 unique colors."""
#    display_name = "Button Color"
#    option_red = 0
#    option_orange = 1
#    option_yellow = 2
#    option_green = 3
#    option_cyan = 4
#    option_blue = 5
#    option_magenta = 6
#    option_purple = 7
#    option_pink = 8
#    option_brown = 9
#    option_white = 10
#    option_black = 11


class LogicDifficulty(Choice):
    """Set the logic difficulty used when generating."""
    display_name = "Logic Difficulty"
    option_easy = 0
    option_no_logic = 4
    default = 0


mmr_options: Dict[str, type(Option)] = {
    "start_inventory_from_pool": StartInventoryPool,
    "logic_difficulty": LogicDifficulty
}
