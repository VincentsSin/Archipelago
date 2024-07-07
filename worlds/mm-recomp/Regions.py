from typing import Dict, List, NamedTuple


class MMRRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, MMRRegionData] = {
    "Menu": MMRRegionData(["Clock Town"]),
    "Clock Town": MMRRegionData(),
}
