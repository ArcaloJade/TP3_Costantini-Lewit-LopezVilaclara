from player import Player
import actions
import random

class Phantom(Player):
    def __init__(self, name, xy, prev_loc = None):
        super().__init__(name, xy, 25)
        self.face = 'P'
        self.type = 'phantom'
        self.prev_loc = prev_loc
        self.alive = True

    def move(self, dungeon, player):
        '''
        Mueve al Phantom segun la posicion del player, priorizando primero igualar su coordenada "y", para luego acercarse en la coordenada "x".
        Si una de las ubicaciones es el player, lo ataca y no se mueve.

        Parametros:
            dungeon: Requiere del mapa para conocer sus alrededores.
            player: Requiere del player para saber cuando atacar.
        '''
        phloc = (self.x, self.y)
        ploc = (player.x, player.y)
        if phloc[1] > ploc[1]:
            new_loc = (phloc[0], phloc[1] - 1)
        elif phloc[1] < ploc[1]:
            new_loc = (phloc[0], phloc[1] + 1)
        elif phloc[0] > ploc[0]:
            new_loc = (phloc[0] - 1, phloc[1])
        elif phloc[0] < ploc[0]:
            new_loc = (phloc[0] + 1, phloc[1])
        if dungeon.is_free(new_loc, player) == True:
            self.x, self.y = new_loc[0], new_loc[1]
        else:
            actions.phantom_attack(player)
            
    def kill(self):
        '''
        Si el Phantom llega a 0 hp, self.alive pasa a ser Falso y cambia self.face a %, representando que alli se encuentra el cadaver.
        '''
        self.hp = 0
        self.alive = False
        self.face = '%'