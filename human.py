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
    
    def _str_(self):
        return f"{self.name}\t\tHP: {self.hp}/{self.max_hp}\t\tTool: {self.tool}\t\tWeapon: {self.weapon}\t\tTreasure: {self.treasure}"

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