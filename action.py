def attack(player, enemy):
        enemy.health_point = enemy.health_point - player.attack if enemy.health_point > player.attack else 0