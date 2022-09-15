#!/usr/bin/env python3
import magic
import actions
from human import Human
from gnome import Gnome
from phantom import Phantom
from items import Item, PickAxe, Sword, Amulet, Shield
from mapping import Dungeon

if __name__ == "__main__":
    # Initial parameters
    level = 0
    ROWS = 25
    COLUMNS = 80
    dungeon = Dungeon(ROWS, COLUMNS, 3)
    turns = 0

    # Player
    player = Human(input("Player?: "), dungeon.find_free_tile())

    # Items
    pickaxe = PickAxe('Pickaxe', '(')
    sword = Sword('Sword', '/')
    amulet = Amulet('Amulet', '"')
    shield = Shield('Shield', 'O')

    # Gnomes
    gnome1 = Gnome('Gnome 1', dungeon.find_free_tile())
    gnome2 = Gnome('Gnome 2', dungeon.find_free_tile())
    gnome3 = Gnome('Gnome 3', dungeon.find_free_tile())

    # Phantom
    phantom1 = Phantom('Phantom 1', dungeon.find_free_tile())
    
    # Adding Items
    pickaxe_location = dungeon.find_free_tile()
    while not dungeon.are_connected(pickaxe_location, (player.x, player.y)):
        pickaxe_location = dungeon.find_free_tile()
    dungeon.add_item(pickaxe, 1, pickaxe_location)
    dungeon.add_item(sword, 2)
    dungeon.add_item(amulet, 3)
    dungeon.add_item(shield, 2)

    # Magic required
    while dungeon.level >= 0 and player.alive == True:
        turns += 1            

        # Dependiendo del nivel elige que monstruos aparecen y se mueven.
        if dungeon.level == 0:
            enemy = gnome1
            phantom = None
        elif dungeon.level == 1:
            enemy = gnome2
            phantom = None
        elif dungeon.level == 2:
            enemy = gnome3
            phantom = phantom1           
        
        # Informacion de los monstruos (hp)
        if dungeon.level != 2:
            print(f"\n\n\nGnome: {enemy.hp}/{enemy.max_hp}")
        else:
            print(f"\n\n\nGnome: {enemy.hp}/{enemy.max_hp}\t\t\tPhantom: {phantom.hp}/{phantom.max_hp}")

        # Renderizado del mapa, enemigos, y jugador.
        dungeon.render(player, enemy, phantom)

        # Menu
        print(f"{player}\t\tHP: {player.hp}/{player.max_hp}\t\tTool: {player.tool}\t\tWeapon: {player.weapon}\nTurns: {turns}\tLevel: {dungeon.level + 1}\t\tArmor: {player.armor}\t\tTreasure: {player.treasure}")

        # Input del usuario.
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
        
        # Si el gnomo y/o el phantom estan vivos, se mueven.
        if dungeon.enemy_alive(enemy) == True:
            enemy.move(dungeon, player)
        if dungeon.enemy_alive(phantom) == True:
            phantom.move(dungeon, player)

    # Si el player muere, imprime mensaje de muerte dependiendo del nivel en el que esta.
    if player.alive == False:
        if dungeon.level != 2:
            print("The gnomes rejoice at your tragic death.")
        else:
            print("A phantom has found its new home.")
            
    # Si gana el juego y cumple el/los requisitos, recive uno o mas ACHIEVEMENTS.
    if player.alive == True and dungeon.level < 0 and player.treasure != None:
        if player.hp == 50:
            print("\nYou've won an achievement: UNSCATHED.\nYou've escaped with te treasure without being hurt.")
        elif player.hp == 1:
            print("\nYou've won an achievement: DIVINE INTERVENTION.\nThe gods have blessed you. You escaped with 1/50 HP.")
        if gnome1.alive == False and gnome2.alive == False and gnome3.alive == False and phantom1.alive == False:
            print("\nYou've won an achievement: GENOCIDAL.\nYou've killed every entity in the dungeon.")
        if gnome1.alive == True and gnome2.alive == True and gnome3.alive == True and phantom1.alive == True:
            print("\nYou've won an achievement: PACIFIST.\nYou left the dungeon without killing any entity.")
        if player.weapon == None and (gnome1.alive == False or gnome2.alive == False or gnome3.alive == False or phantom1.alive == False):
            print("\nYou've won an achievement: WRESTLER.\nYou've killed at least one entity without even picking up the sword.")
        if player.armor == None:
            print("\nYou've won an achievement: DAREDEVIL\nYou've completed the game without the shield. Savage.")