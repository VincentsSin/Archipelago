from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld

def can_play_song(song, state, player):
    return state.has(song, player) and state.has("Ocarina of Time", player)

def can_get_magic_beans(state, player):
    return state.has("Magic Bean", player) or (state.has("Deku Mask", player) and state.can_reach("Deku Palace", 'Region', player))

def has_bombchus(state, player):
    return state.has("Bombchu (1)", player) or state.has("Bombchu (5)", player) or state.has("Bombchu (10)", player)

def has_explosives(state, player):
    return state.has("Progressive Bomb Bag", player) or has_bombchus(state, player)

def has_projectiles(state, player):
    return state.has("Progressive Bow", player) or (state.has("Deku Mask", player) and state.has("Progressive Magic Upgrade", player)) or state.has("Zora Mask", player) or state.has("Hookshot", player)

def can_smack_hard(state, player):
    return state.has("Progressive Sword", player) or state.has("Great Fairy Sword", player) or state.has("Goron Mask", player) or state.has("Zora Mask", player)

def can_smack(state, player):
    return can_smack_hard(state, player) or state.has("Deku Mask", player)

def can_clear_woodfall(state, player):
    return state.can_reach("Woodfall Temple Odolwa's Remains", 'Location', player)

def has_paper(state, player):
    return state.has("Land Title Deed", player) or state.has("Swamp Title Deed", player) or state.has("Mountain Title Deed", player) or state.has("Ocean Title Deed", player) or state.has("Letter to Kafei", player) or state.has("Priority Mail", player)

def has_bottle(state, player):
    return state.has("Bottle", player) or state.has("Bottle of Chateau Romani", player) or state.has("Bottle of Red Potion", player)

def can_plant_beans(state, player):
    return can_get_magic_beans(state, player) and (has_bottle(state, player) or can_play_song("Song of Storms", state, player))

def can_use_powder_keg(state, player):
    return state.has("Powder Keg", player) and state.has("Goron Mask", player)

def can_use_magic_arrow(item, state, player):
    return state.has(item, player) and state.has("Progressive Bow", player) and state.has("Progressive Magic Upgrade", player)

def can_use_fire_arrows(state, player):
    return can_use_magic_arrow("Fire Arrow", state, player)

def can_use_ice_arrows(state, player):
    return can_use_magic_arrow("Ice Arrow", state, player)

def can_use_light_arrows(state, player):
    return can_use_magic_arrow("Light Arrow", state, player)

def has_gilded_sword(state, player):
    return state.has("Progressive Sword", player, 3)

def get_region_rules(player):
    return {
        "Clock Town -> The Moon":
            lambda state: state.has("Ocarina of Time", player) and state.has("Oath to Order", player) and state.has("Odolwa's Remains", player) and state.has("Goht's Remains", player) and state.has("Gyorg's Remains", player) and state.has("Twinmold's Remains", player),
        "Southern Swamp -> Southern Swamp (Deku Palace)":
            lambda state: state.has("Bottle of Red Potion", player) or (has_projectiles(state, player) and state.has("Deku Mask", player)), # or state.has("Pictograph Box")
        "Southern Swamp (Deku Palace) -> Deku Palace":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp (Deku Palace) -> Woodfall":
            lambda state: state.has("Deku Mask", player),
        "Woodfall -> Woodfall Temple":
            lambda state: can_play_song("Sonata of Awakening", state, player),
    }

def get_location_rules(player):
    return {
        "Keaton Quiz":
            lambda state: state.has("Keaton Mask", player),
        "Clock Tower Happy Mask Salesman #1":
            lambda state: state.has("Ocarina of Time", player),
        "Clock Tower Happy Mask Salesman #2":
            lambda state: state.has("Ocarina of Time", player),
        "Clock Town Postbox":
            lambda state: state.has("Postman's Hat", player),
        "Clock Town Hide-and-Seek":
            lambda state: has_projectiles(state, player),
        "Laundry Pool Kafei's Request":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #1":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #2":
            lambda state: state.has("Letter to Kafei", player),
        "South Clock Town Corner Chest":
            lambda state: state.has("Hookshot", player),
        "South Clock Town Final Day Tower Chest":
            lambda state: state.has("Hookshot", player) or (state.has("Deku Mask", player) and state.has("Moon's Tear", player)),
        "East Clock Town Mayor Dotour":
            lambda state: state.has("Couple's Mask", player),
        "East Clock Town Shooting Gallery 40-49 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Shooting Gallery Perfect 50 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Treasure Game Chest":
            lambda state: state.has("Goron Mask", player),
        "East Clock Town Sewer Chest":
            lambda state: has_explosives(state, player),
        "East Clock Town Astral Observatory":
            lambda state: has_projectiles(state, player),
        "North Clock Town Deku Playground Any Day":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Deku Playground All Days":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Old Lady":
            lambda state: state.has("Progressive Sword", player) or state.has("Great Fairy Sword", player),
        "North Clock Town Great Fairy Reward (Transformation Mask)":
            lambda state: state.has("Stray Fairy (Clock Town)", player) and (state.has("Deku Mask", player) or state.has("Goron Mask", player) or state.has("Zora Mask", player)),
        "North Clock Town Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Clock Town)", player),
        "West Clock Town Swordsman Expert Course":
            lambda state: state.has("Progressive Sword", player),
        "West Clock Town Postman Counting":
            lambda state: state.has("Bunny Hood", player),
        "West Clock Town Rosa Sisters":
            lambda state: state.has("Kamaro Mask", player),
        "West Clock Town Bank 200 Rupees":
            lambda state: state.has("Progressive Sword", player) and state.has("Progressive Wallet", player, 2),
        "West Clock Town Bank 1000 Rupees":
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Great Fairy's Sword", player) and state.has("Progressive Wallet", player, 3),
        "West Clock Town Priority Mail to Postman":
            lambda state: state.has("Priority Mail", player),
        "Moon's Tear Trade":
            lambda state: state.has("Moon's Tear", player),
        "Top of Clock Tower (Ocarina of Time)":
            lambda state: has_projectiles(state, player),
        "Top of Clock Tower (Song of Time)":
            lambda state: has_projectiles(state, player),
        "Stock Pot Inn Midnight Meeting":
            lambda state: state.has("Kafei's Mask", player),
        "Stock Pot Inn Knife Chamber Chest":
            lambda state: state.has("Room Key", player),
        "Stock Pot Inn ??? Hand":
            lambda state: has_paper(state, player),
        "Stock Pot Inn Granny Story #1":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Granny Story #2":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Anju and Kafei":
            lambda state: state.has("Letter to Kafei", player) and state.has("Pendant of Memories", player) and state.has("Hookshot", player) and (state.has("Garo Mask", player) or state.has("Gibdo Mask", player)),
        "Milk Bar Show":
            lambda state: state.has("Romani Mask", player) and state.has("Deku Mask", player) and state.has("Goron Mask", player) and state.has("Zora Mask", player) and state.has("Ocarina of Time", player),
        "Milk Bar Priority Mail to Aroma":
            lambda state: state.has("Kafei's Mask", player) and state.has("Priority Mail", player),


        "Termina Stump Chest":
            lambda state: state.has("Hookshot", player) or can_plant_beans(state, player),
        "Termina Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Termina Peahat Grotto Chest":
            lambda state: state.has("Progressive Sword", player),
        "Termina Dodongo Grotto Chest":
            lambda state: state.has("Progressive Sword", player),
        "Termina Kamaro":
            lambda state: state.has("Ocarina of Time", player) and state.has("Song of Healing", player),
        "Milk Road Gorman Ranch Race":
            lambda state: state.has("Ocarina of Time", player) and state.has("Epona's Song", player),
        "Road to Swamp Tree HP":
            lambda state: has_projectiles(state, player),


        "Romani Ranch Grog":
            lambda state: state.has("Bremen Mask", player),
        "Romani Ranch Helping Cremia":
            lambda state: can_use_powder_keg(state, player) and state.has("Progressive Bow", player),


        "Southern Swamp Deku Trade":
            lambda state: state.has("Land Title Deed", player),
        "Southern Swamp Deku Trade Freestanding HP":
            lambda state: state.has("Land Title Deed", player) and state.has("Deku Mask", player),
        "Southern Swamp Koume Tour Gift":
            lambda state: state.has("Bottle of Red Potion", player),
        "Southern Swamp Swamphouse Reward":
            lambda state: can_smack(state, player) and state.has("Sonata of Awakening", player) and state.has("Ocarina of Time", player) and state.has("Deku Mask", player) and (state.has("Hookshot", player) or can_plant_beans(state, player)),
        "Southern Swamp Song Tablet":
            lambda state: state.has("Deku Mask", player),


        "Deku Palace Bean Grotto Chest":
            lambda state: can_plant_beans(state, player) or state.has("Hookshot", player),
        "Deku Palace Monkey Song":
            lambda state: can_plant_beans(state, player),
        "Deku Palace Butler Race":
            lambda state: can_clear_woodfall(state, player) and has_bottle(state, player),
        "Woodfall Near Swamphouse Grotto Chest":
            lambda state: state.has("Deku Mask", player),


        "Woodfall Temple Dragonfly Chest":
            lambda state: state.has("Small Key (Woodfall)", player),
        "Woodfall Temple Black Boe Room Chest":
            lambda state: state.has("Small Key (Woodfall)", player),
        "Woodfall Temple Wooden Flower Switch Chest":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Dinofols Chest":
            lambda state: state.has("Progressive Bow", player) and can_smack_hard(state, player),
        "Woodfall Temple Boss Key Chest":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Wooden Flower Bubble SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Moving Flower Platform Room Beehive SF":
            lambda state: has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Push Block Skulltula SF":
            lambda state: state.has("Small Key (Woodfall)", player) and can_smack_hard(state, player),
        "Woodfall Temple Push Block Bubble SF":
            lambda state: state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Push Block Beehive SF":
            lambda state: state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Final Room Right Lower Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Right Upper Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Left Upper Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Bubble SF":
            lambda state: state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Heart Container":
            lambda state: state.has("Progressive Bow", player) and (state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player)),
        "Woodfall Temple Odolwa's Remains":
            lambda state: state.has("Progressive Bow", player) and (state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player)),


        "Road to Ikana Pillar Chest":
            lambda state: state.has("Hookshot", player),
        "Road to Ikana Rock Grotto Chest":
            lambda state: state.has("Goron Mask", player),


        "Defeat Majora":
            lambda state: state.has("Progressive Magic Upgrade", player) and (state.has("Fierce Deity's Mask", player) or (state.has("Great Fairy Sword", player) or has_gilded_sword(state, player)) and state.has("Progressive Bow", player))
    }
