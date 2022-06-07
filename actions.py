from typing import Union


import mapping
import player
import human
import items
import random

numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(player, enemy):
    if player.weapon == None:
        dmg = random.randint(1, 5)
    else:
        dmg = random.randint(10, 15)
    enemy.hp -= dmg
    if enemy.hp <= 0:
        enemy.kill()
        
def gnome_attack(player):
    dmg = random.randint(2, 6)
    player.hp -= dmg
    if player.hp <= 0:
        player.kill()
        print('You were slain...')
        
def phantom_attack(player):
    dmg = random.randint(5, 10)
    player.hp -= dmg
    if player.hp <= 0:
        player.kill()
        print('You were slain...')


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric], gnome, phantom):
    x = clip(location[0], 0, 79)
    y = clip(location[1],0 , 24)
    if dungeon.is_walkable(location):
        if dungeon.is_free(location, gnome) == True and dungeon.is_free(location, phantom) == True:
            player.move_to((x,y))
        elif dungeon.is_free(location, gnome) == False:
            if gnome.face != '%':
                attack(player, gnome)
            else:
                player.move_to((x,y))
        elif dungeon.is_free(location, phantom) == False:
            if phantom.face != '%':
                attack(player, phantom)
            else:
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
                print(f"You recovered the treasure, {player}!\nBards will sing of your bravery for centuries to come!")
            else:
                print("You returned to the village without any treasure...")
                endings = [1, 2, 3, 4, 5]
                pick = random.choice(endings)
                if pick == 1:
                    print("You have no money to pay your debts, and end up poor and destitute...")
                elif pick == 2:
                    print("The angry mob sends you back to the dungeon. The gnomes and phantoms prove to be too much to handle...")
                elif pick == 3:
                    print("You give your King a fake treasure. Your trick is successful, but the village is soon raided and no one survives...")
                elif pick == 4:
                    print("Ashamed by your deed, your entire family abandons you.")
                elif pick == 5:
                    print("Imperial forces take control of the amulet instead, and use it to turn the entire village into ashes.")
                else:
                    print("Did you think hacking the system would let you win?\nYou poor fool...\nYou die a horrible death for the scum you are.")
        else:
            dungeon.level -= 1
            newstair = dungeon.index(mapping.STAIR_DOWN)
            player.move_to(newstair)

def lose_message(player: human.Human):
    endings = [
    "You have no money to pay your debts, and end up poor and destitute...",
    "The angry mob sends you back to the dungeon. The gnomes and phantoms prove to be too much to handle...",
    "You give your King a fake treasure. Your trick is successful, but the village is soon raided and no one survives...",
    "Ashamed by your deed, your entire family abandons you.",
    "Imperial forces take control of the amulet instead, and use it to turn the entire village into ashes.",
    ]
    if player.treasure != None:
        print(f"You recovered the treasure, {player}!\nBards will sing of your bravery for centuries to come!")
    else:
        print(random.choice(endings))

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