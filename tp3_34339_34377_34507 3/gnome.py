from player import Player
import actions
import random

class Gnome(Player):
    def __init__(self, name, xy, prev_loc = None):
        super().__init__(name, xy, 35)
        self.face = 'G'
        self.type = 'gnome'
        self.prev_loc = prev_loc
        self.alive = True

    def move(self, dungeon, player):
        '''
        Mueve al Gnomo a una de las ubicaciones posibles, ignorando, si es posible, la ubicacion anterior.
        Si una de las ubicaciones es el player, lo ataca y no se mueve.

        Parametros:
            dungeon: Requiere del mapa para conocer sus alrededores.
            player: Requiere del player para saber cuando atacar.
        '''
        walkable = []
        for i in range(4):
            x, y = self.x, self.y
            if i == 0:
                x += 1
            elif i == 1:
                x -= 1
            elif i == 2:
                y += 1
            elif i == 3:
                y -= 1
            x = actions.clip(x, 0, 79)
            y = actions.clip(y, 0, 24)
            if dungeon.is_walkable((x,y)) and not (x == self.x and y == self.y):
                walkable.append((x,y))
        if (player.x, player.y) in walkable:
            actions.gnome_attack(player)
        else:
            if len(walkable) > 1:
                if self.prev_loc in walkable:
                    walkable.remove(self.prev_loc)
                new_loc = random.choice(walkable)
            elif len(walkable) == 1:
                new_loc = walkable[0]
            else:
                new_loc = (self.x, self.y)
            self.prev_loc = (self.x, self.y)
            self.x, self.y = new_loc[0], new_loc[1]
            
    def kill(self):
        '''
        Si el Gnomo llega a 0 hp, self.alive pasa a ser Falso y cambia self.face a %, representando que alli se encuentra el cadaver.
        '''
        self.hp = 0
        self.alive = False
        self.face = '%'            