from player import Player
import actions
import random
import mapping

class Phantom(Player):
    def __init__(self, name, xy, prev_loc = None):
        super().__init__(name, xy, 25)
        self.face = 'P'
        self.type = 'phantom'
        self.prev_loc = prev_loc
        self.alive = True

    def get_type(self):
        '''Returns the type of the item'''
        return self.type
    
    def attack(self, player):
        dmg = random.randint(5, 10)
        player.hp -= dmg

    def move(self, dungeon, player):
        phloc = (self.x, self.y)
        ploc = (player.x, player.y)
        if phloc[1] > ploc[1]:
            new_loc = (phloc[0], phloc[1] - 1)
        elif phloc[1] < ploc[1]:
            new_loc = (phloc[0], phloc[1] + 1)
        elif phloc[0] > ploc[0]:
            new_loc = (phloc[0] - 1, phloc[1])
        elif phloc[1] < ploc[1]:
            new_loc = (phloc[0] + 1, phloc[1])
        elif dungeon.is_free(new_loc, player) == True:
            self.x, self.y = new_loc[0], new_loc[1]
        else:
            actions.phantom_attack(player)
            
    def kill(self):
        self.hp = 0
        self.alive = False
        self.face = '%'
            

        # if dungeon.is_walkable(location):
            