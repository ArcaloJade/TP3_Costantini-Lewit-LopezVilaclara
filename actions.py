from typing import Union


import mapping
import player
import human

numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(dungeon, player): # completar
    # completar
    raise NotImplementedError


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    x = clip(location[0], 0, 79)
    y = clip(location[1],0 , 24)
    if dungeon.is_walkable(location):
        player.move_to((x,y))
    
    

def move_up(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def move_down(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def move_left(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def move_right(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: human.Human):
    location = player.loc()
    item = dungeon.get_items(location)
    print(item)
    if item != []:
        print('hola')
        if 'Pickaxe' in item:
            print('chau')
            player.has_pickaxe()
        elif 'Sword' in item:
            player.has_sword()
                