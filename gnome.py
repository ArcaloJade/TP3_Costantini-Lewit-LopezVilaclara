from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.face = 'G'
        self.type = 'gnome'

    def get_type(self):
        '''Returns the type of the item'''
        return self.type

    