from typing import Union

numeric = Union[float, int]


class Item:
    def __init__(self, name, fc, type):
        self.name = name
        self.face = fc
        self.type = type

    def get_type(self):
        '''
        Devuelve el tipo del objeto
        '''
        return self.type

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"


class Sword(Item):
    def __init__(self, name: str, fc: str): # Faltan argumentos, se los saqué temporalmente: min_dmg: numeric, max_dmg: numeric 
        super().__init__(name, fc, 'weapon')

class Amulet(Item):
    def __init__(self, name: str, fc: str):
        super().__init__(name, fc, 'treasure')


class PickAxe(Item):
    def __init__(self, name: str, fc: str):
        super().__init__(name, fc, 'tool')

class Shield(Item):
    def __init__(self, name: str, fc: str):
        super().__init__(name, fc, 'armor')
