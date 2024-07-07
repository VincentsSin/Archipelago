from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class MMRItem(Item):
    game = "The Majora's Mask Recompilation"


class MMRItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, MMRItemData] = {
    "Stray Fairy (Clock Town)": MMRItemData(
        code=0x3476942000FE7F,
        type=ItemClassification.progression
    ),
    "Progressive Magic Upgrade": MMRItemData(
        code=0x3476942000FD00,
        type=ItemClassification.progression
    ),
    "Moon's Tear": MMRItemData(
        code=0x34769420000096,
        type=ItemClassification.progression
    ),
    "Land Title Deed": MMRItemData(
        code=0x34769420000097,
        type=ItemClassification.progression
    ),
    "Ocarina of Time": MMRItemData(
        code=0x3476942000004C,
        type=ItemClassification.progression
    ),
    "Heart Piece": MMRItemData(
        code=0x3476942000000C,
        type=ItemClassification.useful,
        num_exist=1
    ),
    "Blue Rupee": MMRItemData(
        code=0x3476942000FF01,
        type=ItemClassification.filler#,
        #can_create=lambda multiworld, player: bool(getattr(multiworld, "hard_mode")[player]),
    ),
    # ~ "A Tin of Mints": MMRItemData(
        # ~ code=7430002#,
        # ~ #can_create=lambda multiworld, player: False  # Only created from `get_filler_item_name`.
    # ~ ),
    # ~ "The Urge to Push": CliqueItemData(
        # ~ type=ItemClassification.progression,
    # ~ ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
