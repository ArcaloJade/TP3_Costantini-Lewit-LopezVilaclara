from player import Player
import actions
import random
import mapping

class Gnome(Player):
    def __init__(self, name, xy, prev_loc = None):
        super().__init__(name, xy, 50)
        self.face = 'G'
        self.type = 'gnome'
        self.prev_loc = prev_loc
        self.alive = True

    def get_type(self):
        '''Returns the type of the item'''
        return self.type
    
    def attack(self, player):
        dmg = random.randint(5, 10)
        player.hp -= dmg

    def move(self, dungeon, player):
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
            if dungeon.is_walkable((x,y)) and not (x == self.x and y == self.y) and ((x,y) != self.prev_loc):
                walkable.append((x,y))
        new_loc = random.choice(walkable)
        if dungeon.is_free(new_loc, player) == True:
            self.prev_loc = (self.x, self.y)
            self.x, self.y = new_loc[0], new_loc[1]
        else:
            actions.gnome_attack(player)
            
    def kill(self):
        self.hp = 0
        self.alive = False
        self.face = '%'
            

        # if dungeon.is_walkable(location):
            