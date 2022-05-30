import random
from player import Player


class Human(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'
    
    def __str__(self):
        return f"{self.name} - {self.tool} - {self.weapon} - {self.hp}"

    def damage(self):
        if self.sword: # cambiar por if self.weapon == 'Sword'
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

    def has_sword(self):
        # completar
        pass

    '???'

    def set_pickaxe(self, item):
        self.tool = item
        # print(item)
    
    def set_sword(self, item):
        self.weapon = item
        # print(item)