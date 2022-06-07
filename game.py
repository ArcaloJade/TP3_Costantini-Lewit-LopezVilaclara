#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from gnome import Gnome
from phantom import Phantom
from items import Item, PickAxe, Sword, Amulet
from mapping import Dungeon
import actions

ROWS = 25
COLUMNS = 80

if __name__ == "__main__":
    # initial parameters
    level = 0
    
    # initial locations may be random generated
    # gnomes = 0

    dungeon = Dungeon(ROWS, COLUMNS, 3)

    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    player = Human(input("Player?: "), dungeon.find_free_tile())

    turns = 0

    # Items
    pickaxe = PickAxe('Pickaxe', '(')
    sword = Sword('Sword', '/')
    amulet = Amulet('Amulet', '"')

    # Gnomes
    gnome1 = Gnome('Gnome 1', dungeon.find_free_tile())
    gnome2 = Gnome('Gnome 2', dungeon.find_free_tile())
    gnome3 = Gnome('Gnome 3', dungeon.find_free_tile())

    # Phantom
    phantom1 = Phantom('Phantom 1', dungeon.find_free_tile())
    
    # Items
    pickaxe_location = dungeon.find_free_tile()
    while dungeon.are_connected(pickaxe_location, (player.x, player.y)) == False:
        pickaxe_location = dungeon.find_free_tile()
    dungeon.add_item(pickaxe, 1, pickaxe_location)
    dungeon.add_item(sword, 2)
    dungeon.add_item(amulet, 3)

    # Os
    os = input('win or mac [w/m]')

    # Windows
    if os == 'w':
        while dungeon.level >= 0 and player.alive == True:
            turns += 1
            # render map
            
            if dungeon.level == 0:
                enemy = gnome1
                phantom = None
            elif dungeon.level == 1:
                enemy = gnome2
                phantom = None
            elif dungeon.level == 2:
                enemy = gnome3
                phantom = phantom1

            # enemy = gnomes[dungeon.level]
            
            # print(f"Gnome 1: {gnome1.hp}/{gnome1.max_hp}/t/t/tGnome 2: {gnome2.hp}/{gnome2.max_hp}/t/t/tGnome 3: {gnome3.hp}/{gnome3.max_hp}/t/t/tPhantom: {phantom.hp}/{phantom.max_hp}")
            if dungeon.level != 2:
                print(f"Gnome: {enemy.hp}/{enemy.max_hp}")
            else:
                print(f"Gnome: {enemy.hp}/{enemy.max_hp}\t\t\tPhantom: {phantom.hp}/{phantom.max_hp}")
            dungeon.render(player, enemy, phantom)

            print(f"{player}\t\tHP: {player.hp}/{player.max_hp}\t\tTool: {player.tool}\t\tWeapon: {player.weapon}\nTurns: {turns}\tLevel: {dungeon.level + 1}\t\tTreasure: {player.treasure}")

            key2 = input()

            dungeon.render(player, enemy, phantom)
            if key2 == 'q':
                break
            if key2 == 'w':
                actions.move_to(dungeon, player, (player.x, player.y - 1), enemy, phantom)
            elif key2 == 'a':
                actions.move_to(dungeon, player, (player.x - 1, player.y), enemy, phantom)
            elif key2 == 's':
                actions.move_to(dungeon, player, (player.x, player.y + 1), enemy, phantom)
            elif key2 == 'd':
                actions.move_to(dungeon, player, (player.x + 1, player.y), enemy, phantom)
            elif key2 == 'p':
                actions.pickup(dungeon, player)
            elif key2 == 'u':
                actions.climb_stair(dungeon, player)
            elif key2 == 'v':
                actions.descend_stair(dungeon, player)
                # Pick up an object

            if dungeon.enemy_alive(enemy) == True:
                enemy.move(dungeon, player)
            
            if dungeon.enemy_alive(phantom) == True:
                phantom.move(dungeon, player)

            # print(player.hp)
            # print(gnome1.hp)
        if player.alive == False:
            if dungeon.level != 2:
                print("The gnomes rejoice at your tragic death.")
            else:
                print("A phantom has found its new home.")
            
        if player.alive == True and dungeon.level < 0 and player.treasure != None:
            if gnome1.alive == False and gnome2.alive == False and gnome3.alive == False and phantom.alive == False:
                print("\nYou've won an achievement: GENOCIDAL.\nYou've killed every entity in the dungeon.")
            if gnome1.alive == True and gnome2.alive == True and gnome3.alive == True and phantom.alive == True:
                print("\nYou've won an achievement: PACIFIST.\nYou left the dungeon without killing any entity.")
            if player.weapon == None:
                print("\nYou've won an achievement: DAREDEVIL.\nYou've won without even picking up the sword.")
            # if player.hp == 50:
                
            
    # Mac
    elif os == 'm':
        while dungeon.level >= 0 and player.alive == True:
            turns += 1            

            if dungeon.level == 0:
                enemy = gnome1
                phantom = None
            elif dungeon.level == 1:
                enemy = gnome2
                phantom = None
            elif dungeon.level == 2:
                enemy = gnome3
                phantom = phantom1           
            
            if dungeon.level != 2:
                print(f"\n\n\nGnome: {enemy.hp}/{enemy.max_hp}")
            else:
                print(f"\n\n\nGnome: {enemy.hp}/{enemy.max_hp}\t\t\tPhantom: {phantom.hp}/{phantom.max_hp}")
            
            # enemy = gnomes[dungeon.level]

            dungeon.render(player, enemy, phantom)

            print(f"{player}\t\tHP: {player.hp}/{player.max_hp}\t\tTool: {player.tool}\t\tWeapon: {player.weapon}\nTurns: {turns}\tLevel: {dungeon.level + 1}\t\tTreasure: {player.treasure}")

            key = magic.read_single_keypress()

            if key[0] == 'q':
                break
            if key[0] == 'w':
                actions.move_to(dungeon, player, (player.x, player.y - 1), enemy, phantom)
            elif key[0] == 'a':
                actions.move_to(dungeon, player, (player.x - 1, player.y), enemy, phantom)
            elif key[0] == 's':
                actions.move_to(dungeon, player, (player.x, player.y + 1), enemy, phantom)
            elif key[0] == 'd':
                actions.move_to(dungeon, player, (player.x + 1, player.y), enemy, phantom)
            elif key[0] == 'p':
                actions.pickup(dungeon, player)
            elif key[0] == 'u':
                actions.climb_stair(dungeon, player)
            elif key[0] == 'v':
                actions.descend_stair(dungeon, player)
            
            if dungeon.enemy_alive(enemy) == True:
                enemy.move(dungeon, player)

            if dungeon.enemy_alive(phantom) == True:
                phantom.move(dungeon, player)

        if player.alive == False:
            if dungeon.level != 2:
                print("The gnomes rejoice at your tragic death.")
            else:
                print("A phantom has found its new home.")
                
        if player.alive == True and dungeon.level < 0 and player.treasure != None:
            if gnome1.alive == False and gnome2.alive == False and gnome3.alive == False and phantom1.alive == False and player.hp == 50:
                print("\nYou've won an achievement: PERFECT GENOCIDAL.\nYou've killed every entity in the dungeon without losing a single life.")
            elif gnome1.alive == False and gnome2.alive == False and gnome3.alive == False and phantom1.alive == False and player.hp != 50:
                print("\nYou've won an achievement: GENOCIDAL.\nYou've killed every entity in the dungeon.")
            elif gnome1.alive == True and gnome2.alive == True and gnome3.alive == True and phantom1.alive == True:
                print("\nYou've won an achievement: PACIFIST.\nYou left the dungeon without killing any entity.")
            # elif gnome1.alive == False and gnome2.alive == False and gnome3.alive == False and phantom1.alive == True:
