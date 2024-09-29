from emoji import emojize
from character import Enemy
from constants import ENEMIES


def show_battle_status(player, enemy) -> None:
    print("\n{:#^100}\n".format(" Text RPG "))
    print(f"{player.name} {enemy.name:>50}")
    print(f"{emojize(":red_heart:")} HP: {player.health_point} {f"{emojize(":red_heart:")} HP: {enemy.health_point}":>51}")
    print(f"{emojize(":blue_heart:")} MP: {player.mana_point}")
    print()

def action_selector(actions) -> int:
    for key, action in enumerate(actions):
        print(f"{key} - {action}")
    try:
        return int(input("Select: "))
    except ValueError:
        print("Invalid input. Please input only integers")

def choose_enemy() -> Enemy:
    return Enemy(ENEMIES[action_selector(ENEMIES)])

# Wrappers
def wrap_borders(func):
    def wrapper(*args, **kwargs):
        print("\n{:#^100}".format(" Text RPG "))
        func(*args, **kwargs)
    return wrapper