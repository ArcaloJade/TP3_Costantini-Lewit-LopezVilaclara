from typing import Union


import mapping
import player
import human
import items

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
    else:
        if player.tool != None:
            dungeon.dig((x,y))
            

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


def climb_stair(dungeon: mapping.Dungeon, player: human.Human):
    location = player.loc()
    stair = dungeon.index(mapping.STAIR_UP)
    if location == stair:
        if dungeon.level == 0:
            dungeon.level -= 1
            if player.treasure != None:
                print('you won!')
            else:
                print('fracasado de mierda (puto)')
        else:
            dungeon.level -= 1
            newstair = dungeon.index(mapping.STAIR_DOWN)
            player.move_to(newstair)


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    location = player.loc()
    if dungeon.level < 2:
        stair = dungeon.index(mapping.STAIR_DOWN)
        if location == stair:
            dungeon.level += 1
            newstair = dungeon.index(mapping.STAIR_UP)
            player.move_to(newstair)

def pickup(dungeon: mapping.Dungeon, player: human.Human):
    location = player.loc()
    item = dungeon.get_items(location)
    if item != []:
        type = item[0].get_type()
        if item[0].type == 'tool':
            player.tool = item[0]
        elif type == 'weapon':
            player.weapon = item[0]
        elif type == 'treasure':
            player.treasure = item[0]