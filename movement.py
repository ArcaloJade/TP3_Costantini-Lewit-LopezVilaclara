import actions
def movement()
            if key[0] == 'q':
                break
            if key[0] == 'w':
                actions.move_to(dungeon, player, (player.x, player.y - 1), enemy)
            elif key[0] == 'a':
                actions.move_to(dungeon, player, (player.x - 1, player.y), enemy)
            elif key[0] == 's':
                actions.move_to(dungeon, player, (player.x, player.y + 1), enemy)
            elif key[0] == 'd':
                actions.move_to(dungeon, player, (player.x + 1, player.y), enemy)
            elif key[0] == 'p':
                actions.pickup(dungeon, player)
            elif key[0] == 'u':
                actions.climb_stair(dungeon, player)
            elif key[0] == 'v':
                actions.descend_stair(dungeon, player)
            
            if dungeon.enemy_alive(enemy) == True:
                enemy.move(dungeon, player)