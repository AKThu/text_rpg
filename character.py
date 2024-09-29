

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.health_point = 10
        self.mana_point = 10
        self.attack = 2
        self.defence = 2

class Enemy:
    def __init__(self, name) -> None:
        self.name = name
        self.health_point = 5
        self.attack = 1
        self.defence = 1