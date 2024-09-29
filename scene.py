from helpers import action_selector, wrap_borders, show_battle_status, choose_enemy
from global_var import player
from action import attack
from color import Color, format_color
from constants import LOCATIONS


@wrap_borders
def change_location(current_location: str) -> None:
    target_location_index = action_selector(LOCATIONS[current_location])
    target_location = LOCATIONS[current_location][target_location_index]
    if target_location == "exit game":
        exit()
    elif target_location == "fight monster":
        fight_scene()
    elif target_location == "buy items":
        shop_scene()
    elif target_location in LOCATIONS.keys():
        change_location(target_location)
    else:
        print("Invalid command")


def fight_scene():
    enemy = choose_enemy()
    show_battle_status(player, enemy)
    while enemy.health_point != 0:
        action = action_selector([ "Attack", "Run" ])
        show_battle_status(player, enemy)
        if action == 0:
            attack(player, enemy)
            if enemy.health_point <= 0:
                # print text "Player defeated Enemy"
                print(format_color("{:^100}".format(f"{player.name} defeated {enemy.name}"), Color.green))
            else:
                # print text "Player deals damage to Enemy"
                print(format_color("{:^100}".format(f"{player.name} deals {player.attack} damage to {enemy.name}"), Color.red))
        elif action == 1:
            print(f"{player.name} runs away")
            break
    change_location("forest")

def shop_scene():
    print("shopping items")