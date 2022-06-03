from player import Player
import mapping

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.face = 'G'
        self.type = 'monster'
        self.alive = True

    def get_type(self):
        '''Returns the type of the item'''
        return self.type
    
    def move_gnome(self, walkable = []):
        xy = self.loc()
        surroundings = ((xy[0],xy[1]-1), (xy[0]-1,xy[1]), (xy[0],xy[1]+1), (xy[0] + 1, xy[1])) # Tupla de tuplas, en orden: W, A, S, D.
        for tile in surroundings:
            if mapping.Level.is_walkable(tile) == True:
                walkable.append(tile)
            else:
                continue
        if len(walkable) == 1:
            self.xy = walkable[0]
            
                

class Phantom(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 40)
        self.face = 'P'
        self.type = 'monster'
        self.alive = True
        
        