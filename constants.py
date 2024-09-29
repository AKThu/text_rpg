START_LOCATION = "home"

LOCATIONS = {
    START_LOCATION: [
        "exit game",
        "town",
        "forest"
    ],
    "town": [
        START_LOCATION,
        "shop"
    ],
    "forest": [
        START_LOCATION,
        "fight monster"
    ],
    "shop": [
        "town",
        "buy items"
    ]
}

ENEMIES = [
    "goblin",
    "wolf",
    "ogre",
    "dragon"
]