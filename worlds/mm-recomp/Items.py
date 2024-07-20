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
        code=0x3476942001007F,
        type=ItemClassification.progression
    ),
    "Progressive Magic Upgrade": MMRItemData(
        code=0x34769420020000,
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
    "Swamp Title Deed": MMRItemData(
        code=0x34769420000098,
        type=ItemClassification.progression
    ),
    "Mountain Title Deed": MMRItemData(
        code=0x34769420000099,
        type=ItemClassification.progression
    ),
    "Ocean Title Deed": MMRItemData(
        code=0x3476942000009A,
        type=ItemClassification.progression
    ),
    "Ocarina of Time": MMRItemData(
        code=0x3476942000004C,
        type=ItemClassification.progression,
        can_create=lambda multiworld, player: False
    ),
    "Heart Piece": MMRItemData(
        code=0x3476942000000C,
        type=ItemClassification.useful,
        num_exist=52
    ),
    "Adult's Wallet": MMRItemData(
        code=0x34769420000008,
        type=ItemClassification.progression
    ),
    "Giant's Wallet": MMRItemData(
        code=0x34769420000009,
        type=ItemClassification.progression
    ),
    "Sonata of Awakening": MMRItemData(
        code=0x34769420040061,
        type=ItemClassification.progression
    ),
    "Goron's Lullaby": MMRItemData(
        code=0x34769420040062,
        type=ItemClassification.progression
    ),
    "New Wave Bossa Nova": MMRItemData(
        code=0x34769420040063,
        type=ItemClassification.progression
    ),
    "Elegy of Emptiness": MMRItemData(
        code=0x34769420040064,
        type=ItemClassification.progression
    ),
    "Oath to Order": MMRItemData(
        code=0x34769420040065,
        type=ItemClassification.progression
    ),
    "Song of Time": MMRItemData(
        code=0x34769420040067,
        type=ItemClassification.progression,
        can_create=lambda multiworld, player: False
    ),
    "Song of Healing": MMRItemData(
        code=0x34769420040068,
        type=ItemClassification.progression
    ),
    "Epona's Song": MMRItemData(
        code=0x34769420040069,
        type=ItemClassification.progression
    ),
    "Song of Soaring": MMRItemData(
        code=0x3476942004006A,
        type=ItemClassification.progression
    ),
    "Deku Mask": MMRItemData(
        code=0x34769420000078,
        type=ItemClassification.progression
    ),
    "Goron Mask": MMRItemData(
        code=0x34769420000079,
        type=ItemClassification.progression
    ),
    "Zora Mask": MMRItemData(
        code=0x3476942000007A,
        type=ItemClassification.progression
    ),
    "Fierce Deity's Mask": MMRItemData(
        code=0x3476942000007B,
        type=ItemClassification.progression
    ),
    "Captain's Hat": MMRItemData(
        code=0x3476942000007C,
        type=ItemClassification.progression
    ),
    "Giant's Mask": MMRItemData(
        code=0x3476942000007D,
        type=ItemClassification.progression
    ),
    "All-Night Mask": MMRItemData(
        code=0x3476942000007E,
        type=ItemClassification.progression
    ),
    "Bunny Hood": MMRItemData(
        code=0x3476942000007F,
        type=ItemClassification.progression
    ),
    "Keaton Mask": MMRItemData(
        code=0x34769420000080,
        type=ItemClassification.progression
    ),
    "Garo Mask": MMRItemData(
        code=0x34769420000081,
        type=ItemClassification.progression
    ),
    "Romani Mask": MMRItemData(
        code=0x34769420000082,
        type=ItemClassification.progression
    ),
    "Circus Leader's Mask": MMRItemData(
        code=0x34769420000083,
        type=ItemClassification.progression
    ),
    "Postman's Hat": MMRItemData(
        code=0x34769420000084,
        type=ItemClassification.progression
    ),
    "Couple's Mask": MMRItemData(
        code=0x34769420000085,
        type=ItemClassification.progression
    ),
    "Great Fairy Mask": MMRItemData(
        code=0x34769420000086,
        type=ItemClassification.progression
    ),
    "Gibdo Mask": MMRItemData(
        code=0x34769420000087,
        type=ItemClassification.progression
    ),
    "Don Gero Mask": MMRItemData(
        code=0x34769420000088,
        type=ItemClassification.progression
    ),
    "Kamaro Mask": MMRItemData(
        code=0x34769420000089,
        type=ItemClassification.progression
    ),
    "Mask of Truth": MMRItemData(
        code=0x3476942000008A,
        type=ItemClassification.progression
    ),
    "Stone Mask": MMRItemData(
        code=0x3476942000008B,
        type=ItemClassification.progression
    ),
    "Bremen Mask": MMRItemData(
        code=0x3476942000008C,
        type=ItemClassification.progression
    ),
    "Blast Mask": MMRItemData(
        code=0x3476942000008D,
        type=ItemClassification.progression
    ),
    "Mask of Scents": MMRItemData(
        code=0x3476942000008E,
        type=ItemClassification.progression
    ),
    "Kafei's Mask": MMRItemData(
        code=0x3476942000008F,
        type=ItemClassification.progression
    ),
    "Room Key": MMRItemData(
        code=0x347694200000A0,
        type=ItemClassification.progression
    ),
    "Letter to Kafei": MMRItemData(
        code=0x347694200000AA,
        type=ItemClassification.progression
    ),
    "Pendant of Memories": MMRItemData(
        code=0x347694200000AB,
        type=ItemClassification.progression
    ),
    "Priority Mail": MMRItemData(
        code=0x347694200000A1,
        type=ItemClassification.progression
    ),
    "Bottle of Chateau Romani": MMRItemData(
        code=0x3476942000006F,
        type=ItemClassification.progression
    ),
    "Kokiri Sword": MMRItemData(
        code=0x34769420000037,
        type=ItemClassification.progression,
        can_create=lambda multiworld, player: False
    ),
    "Razor Sword": MMRItemData(
        code=0x34769420000038,
        type=ItemClassification.progression
    ),
    "Gilded Sword": MMRItemData(
        code=0x34769420000039,
        type=ItemClassification.progression
    ),
    "Great Fairy Sword": MMRItemData(
        code=0x3476942000003B,
        type=ItemClassification.progression
    ),
    "Hero's Bow": MMRItemData(
        code=0x34769420000022,
        type=ItemClassification.progression
    ),
    "Large Quiver": MMRItemData(
        code=0x34769420000023,
        type=ItemClassification.progression
    ),
    "Largest Quiver": MMRItemData(
        code=0x34769420000024,
        type=ItemClassification.progression
    ),
    "Fire Arrow": MMRItemData(
        code=0x34769420000025,
        type=ItemClassification.progression
    ),
    "Ice Arrow": MMRItemData(
        code=0x34769420000026,
        type=ItemClassification.progression
    ),
    "Light Arrow": MMRItemData(
        code=0x34769420000027,
        type=ItemClassification.progression
    ),
    "Pictograph Box": MMRItemData(
        code=0x34769420000043,
        type=ItemClassification.progression
    ),
    "Lens of Truth": MMRItemData(
        code=0x34769420000042,
        type=ItemClassification.progression
    ),
    "Hookshot": MMRItemData(
        code=0x34769420000041,
        type=ItemClassification.progression
    ),
    "Mirror Shield": MMRItemData(
        code=0x34769420000033,
        type=ItemClassification.progression
    ),
    "Magic Bean": MMRItemData(
        code=0x34769420000035,
        type=ItemClassification.progression
    ),
    "Bottle of Red Potion": MMRItemData(
        code=0x34769420000059,
        type=ItemClassification.progression
    ),
    "Blue Potion": MMRItemData(
        code=0x3476942000005D,
        type=ItemClassification.progression
    ),
    "Stray Fairy (Woodfall)": MMRItemData(
        code=0x34769420010001,
        type=ItemClassification.progression,
        num_exist=15
    ),
    "Stray Fairy (Snowhead)": MMRItemData(
        code=0x34769420010002,
        type=ItemClassification.progression,
        num_exist=15
    ),
    "Stray Fairy (Great Bay)": MMRItemData(
        code=0x34769420010003,
        type=ItemClassification.progression,
        num_exist=15
    ),
    "Stray Fairy (Stone Tower)": MMRItemData(
        code=0x34769420010004,
        type=ItemClassification.progression,
        num_exist=15
    ),
    "Small Key (Woodfall)": MMRItemData(
        code=0x34769420090178,
        type=ItemClassification.progression,
        num_exist=1
    ),
    "Small Key (Snowhead)": MMRItemData(
        code=0x34769420090278,
        type=ItemClassification.progression,
        num_exist=3
    ),
    "Small Key (Great Bay)": MMRItemData(
        code=0x34769420090378,
        type=ItemClassification.progression,
        num_exist=1
    ),
    "Small Key (Stone Tower)": MMRItemData(
        code=0x34769420090478,
        type=ItemClassification.progression,
        num_exist=3
    ),
    "Dungeon Map (Woodfall)": MMRItemData(
        code=0x34769420090176,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Snowhead)": MMRItemData(
        code=0x34769420090276,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Great Bay)": MMRItemData(
        code=0x34769420090376,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Stone Tower)": MMRItemData(
        code=0x34769420090476,
        type=ItemClassification.useful
    ),
    "Compass (Woodfall)": MMRItemData(
        code=0x34769420090175,
        type=ItemClassification.useful
    ),
    "Compass (Snowhead)": MMRItemData(
        code=0x34769420090275,
        type=ItemClassification.useful
    ),
    "Compass (Great Bay)": MMRItemData(
        code=0x34769420090375,
        type=ItemClassification.useful
    ),
    "Compass (Stone Tower)": MMRItemData(
        code=0x34769420090475,
        type=ItemClassification.useful
    ),
    "Boss Key (Woodfall)": MMRItemData(
        code=0x34769420090174,
        type=ItemClassification.progression
    ),
    "Boss Key (Snowhead)": MMRItemData(
        code=0x34769420090274,
        type=ItemClassification.progression
    ),
    "Boss Key (Great Bay)": MMRItemData(
        code=0x34769420090374,
        type=ItemClassification.progression
    ),
    "Boss Key (Stone Tower)": MMRItemData(
        code=0x34769420090474,
        type=ItemClassification.progression
    ),
    "Odolwa's Remains": MMRItemData(
        code=0x34769420000055,
        type=ItemClassification.progression
    ),
    "Goht's Remains": MMRItemData(
        code=0x34769420000056,
        type=ItemClassification.progression
    ),
    "Gyorg's Remains": MMRItemData(
        code=0x34769420000057,
        type=ItemClassification.progression
    ),
    "Twinmold's Remains": MMRItemData(
        code=0x34769420000058,
        type=ItemClassification.progression
    ),
    "Bomb Bag": MMRItemData(
        code=0x3476942000001B,
        type=ItemClassification.progression
    ),
    "Big Bomb Bag": MMRItemData(
        code=0x3476942000001C,
        type=ItemClassification.progression
    ),
    "Biggest Bomb Bag": MMRItemData(
        code=0x3476942000001D,
        type=ItemClassification.progression
    ),
    "Bombchu (1)": MMRItemData(
        code=0x34769420000036,
        type=ItemClassification.useful,
        num_exist=4
    ),
    "Bombchu (5)": MMRItemData(
        code=0x3476942000003A,
        type=ItemClassification.useful,
        num_exist=1
    ),
    "Bombchu (10)": MMRItemData(
        code=0x3476942000001A,
        type=ItemClassification.progression,
        num_exist=1
    ),
    "Blue Rupee": MMRItemData(
        code=0x34769420000002,
        type=ItemClassification.filler,
        num_exist=2
    ),
    "Red Rupee": MMRItemData(
        code=0x34769420000004,
        type=ItemClassification.filler,
        num_exist=23
    ),
    "Purple Rupee": MMRItemData(
        code=0x34769420000005,
        type=ItemClassification.useful,
        num_exist=6
    ),
    "Silver Rupee": MMRItemData(
        code=0x34769420000006,
        type=ItemClassification.useful,
        num_exist=9
    ),
    # ~ "Blue Rupee": MMRItemData(
        # ~ code=0x34769420000002,
        # ~ type=ItemClassification.filler#,
        # ~ #can_create=lambda multiworld, player: bool(getattr(multiworld, "hard_mode")[player]),
    # ~ ),
    # ~ "A Tin of Mints": MMRItemData(
        # ~ code=7430002#,
        # ~ #can_create=lambda multiworld, player: False  # Only created from `get_filler_item_name`.
    # ~ ),
    # ~ "The Urge to Push": CliqueItemData(
        # ~ type=ItemClassification.progression,
    # ~ ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
