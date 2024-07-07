from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class MMRLocation(Location):
    game = "The Majora's Mask Recompilation"


class MMRLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, MMRLocationData] = {
    "Laundry Pool Stray Fairy (Clock Town)": MMRLocationData(
        region="Clock Town",
        address=0x3476942000FE7F
    ),
    "Great Fairy Reward (Clock Town)": MMRLocationData(
        region="Clock Town",
        address=0x3476942000FC00
    ),
    "Astral Observatory": MMRLocationData(
        region="Clock Town",
        address=0x34769420000096
    ),
    "Land Title Trade": MMRLocationData(
        region="Clock Town",
        address=0x34769420000097
    ),
    "Top of Clock Tower": MMRLocationData(
        region="Clock Town",
        address=0x3476942000004C
    ),
    "Heart Piece (South Clock Town)": MMRLocationData(
        region="Clock Town",
        address=0x34769420006F0A
    ),
    #"The Item on the Desk": CliqueLocationData(
    #    region="The Button Realm",
    #    address=69696968,
    #    can_create=lambda multiworld, player: bool(getattr(multiworld, "hard_mode")[player]),
    #),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
