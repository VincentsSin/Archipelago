from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState


class MMRRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, MMRRegionData] = {
    "Menu": MMRRegionData(["Clock Town"]),
    "Clock Town": MMRRegionData(["Termina Field", "The Moon"]),
    "The Moon": MMRRegionData([]),
    "Termina Field": MMRRegionData(["Southern Swamp", "Romani Ranch"]),
    "Southern Swamp": MMRRegionData(["Southern Swamp (Deku Palace)"]),
    "Romani Ranch": MMRRegionData([]),
    "Southern Swamp (Deku Palace)": MMRRegionData(["Deku Palace", "Woodfall"]),
    "Deku Palace": MMRRegionData([]),
    "Woodfall": MMRRegionData(["Woodfall Temple"]),
    "Woodfall Temple": MMRRegionData([]),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
