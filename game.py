#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from items import Item, PickAxe, Sword, Amulet
from mapping import Dungeon
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    

    # initial locations may be random generated
    gnomes = 0

    dungeon = Dungeon(ROWS, COLUMNS, 3)

    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    player = Human(input("Player?: "), dungeon.find_free_tile())

    turns = 0

    pickaxe = PickAxe('Pickaxe', '(')
    sword = Sword('Sword', '/')
    amulet = Amulet('Amulet', '"')

    dungeon.add_item(pickaxe, 1)
    dungeon.add_item(sword, 2)
    dungeon.add_item(amulet, 3)

    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render(player)
        # dungeon.render() (Para el gnome, falta completar!)
        # read key

        key = magic.read_single_keypress()

        # key = input()
        
        if key[0] == 'q':
            break

        if key[0] == 'w':
            actions.move_to(dungeon, player, (player.x, player.y - 1))
        elif key[0] == 'a':
            actions.move_to(dungeon, player, (player.x - 1, player.y))
        elif key[0] == 's':
            actions.move_to(dungeon, player, (player.x, player.y + 1))
        elif key[0] == 'd':
            actions.move_to(dungeon, player, (player.x + 1, player.y))
        elif key[0] == 'p':
            actions.pickup(dungeon, player)
            # Pick up an object
        elif key[0] == '`':
            print(player)
        
        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego