from typing import Union

import mapping
import player
import human
import random

numeric = Union[int, float]

def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(player, enemy):
    '''
    Esta funcion permite al jugador atacar entidades. Si se posee la espada, el dano causado sera randomizado entre 10 y 15.
    Caso contrario, sera randomizado entre 3 y 5.

    Parametros:
        player: El jugador, necesario para verificar si se posee la espada.
        enemy: El enemigo. Puede ser un Phantom o un Gnomo.
    '''
    if player.weapon == None:
        dmg = random.randint(3, 5)
    else:
        dmg = random.randint(10, 15)
    enemy.hp -= dmg
    if enemy.hp <= 0:
        enemy.kill()
        
def gnome_attack(player):
    '''
    Esta funcion le permite al Gnomo atacar al jugador. 
    Si el jugador posee el escudo, recibira menos dano (entre 2 y 6) que si no lo tiene (entre 5 y 10)
    Si con un ataque player.hp (la vida del jugador) llega a 0, imprime un mensaje y corre la funcion correspondiente.

    Parametros:
        player: El jugador, usado para verificar si se posee el escudo y para actualizar su vida luego de un ataque.
    '''
    if player.armor == None:
        dmg = random.randint(5, 10)
    else:
        dmg = random.randint(2, 6)
    player.hp -= dmg
    if player.hp <= 0:
        player.kill()
        print('You were slain...')
        
def phantom_attack(player):
    '''
    Esta funcion le permite al Phantom atacar al jugador. 
    Si el jugador posee el escudo, recibira menos dano (entre 2 y 6) que si no lo tiene (entre 5 y 10)
    Si con un ataque player.hp (la vida del jugador) llega a 0, imprime un mensaje y corre la funcion correspondiente.

    Parametros:
        player: El jugador, usado para verificar si se posee el escudo y para actualizar su vida luego de un ataque.
    '''
    if player.armor == None:
        dmg = random.randint(10, 15)
    else:
        dmg = random.randint(5, 10)
    player.hp -= dmg
    if player.hp <= 0:
        player.kill()
        print('You were slain...')


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric], gnome, phantom):
    '''
    Esta funcion permite el movimiento del jugador. Para hacerlo, controla que:
        -No se superen los limites del mapa.
        -Si no se tiene el pico, no permite caminar en las paredes.
        -Si se tiene el pico y hay una pared, rompe la pared, permitiendo que en el proximo turno se pueda mover alli.
        -Si hay una entidad viva, no permite el movimiento y la ataca.

    Parametros:
        dungeon: El mapa, necesario para conocer los alrededores.
        player: El jugador, necesario para ejecutar metodos de su clase y verificar si posee el pico
        location: Tupla donde el jugador se esta intentando mover.
        gnome: La entidad Gnomo correspondiente al nivel.
        phantom: La entidad Phantom correspondiente al nivel.
    '''
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

def climb_stair(dungeon: mapping.Dungeon, player: human.Human):
    '''
    Permite al jugador subir escaleras. Si el mismo se encuentra en el nivel 1, termina el juego.
    A la hora de terminarlo, se fija si el jugador tiene el tesoro. Si lo tiene, imprime el mensaje correspondiente, notificando que gano.
    Si no lo tiene, imprime uno de los posibles mensajes correspondientes a la hora de perder.
    
    Parametros:
        dungeon: El mapa, necesario para conocer el nivel y la ubicacion de las escaleras.
        player: EL jugador, necesario para conocer su posicion y ejecutar metodos correspondientes.
    '''
    location = player.loc()
    stair = dungeon.index(mapping.STAIR_UP)
    if location == stair:
        if dungeon.level == 0:
            dungeon.level -= 1
            end_message()
        else:
            dungeon.level -= 1
            newstair = dungeon.index(mapping.STAIR_DOWN)
            player.move_to(newstair)

def end_message(player: human.Human):
    '''
    Funcion ejecutada al finalizar el juego.
    Si el jugador gano, imprime el mensaje correspondiente.
    Si perdio, se encarga de elegir de manera aleatoria entre los mensajes de endings.

    Parametros:
        player: El jugador, necesario para verificar si posee el tesoro o no.
    '''
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
    '''
    Permite al jugador bajar esaleras.

    Parametros:
        dungeon: El mapa, necesario para conocer el nivel y la ubicacion de las escaleras.
        player: EL jugador, necesario para conocer su posicion y ejecutar metodos correspondientes.
    '''
    location = player.loc()
    if dungeon.level < 2:
        stair = dungeon.index(mapping.STAIR_DOWN)
        if location == stair:
            dungeon.level += 1
            newstair = dungeon.index(mapping.STAIR_UP)
            player.move_to(newstair)

def pickup(dungeon: mapping.Dungeon, player: human.Human):
    '''
    Esta funcion permite al jugador interactuar con los objetos renderizados. Permite agarrar objetos del tipo Item,
    sacandolos del mapa y actualizando en el jugador las variables player.type, donde type es el tipo de Item (tool, weapon, treasure, armor)

    Parametros:
        dungeon: El mapa, necesario para ejecutar metodos correspondientes.
        player: El jugador, necesario para conocer su ubicacion y actualizar player.tool, player.weapon, player.treasure, player.armor.
    '''
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
        elif type == 'armor':
            player.armor = item[0]