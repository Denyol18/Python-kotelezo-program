"""Játéktér scriptje"""

import pygame as pg

# Játéktér kialakítása

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, 2, 2, _, _, _, _, _, 3, 3, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 1],
    [1, _, _, 2, _, 2, _, _, _, _, 3, _, _, _, _, 1],
    [1, _, _, 2, _, 2, _, _, _, _, 3, 3, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    """A játékteret reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        """Játékteret lekérő és létrehozó függvény"""

        for i, row in enumerate(self.mini_map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j, i)] = value

    def draw(self):
        """A játékteret megrajzoló függvény debugging célból"""

        [pg.draw.rect(self.game.screen, 'green',
                      (pos[0] * 80, pos[1] * 80, 80, 80), 2)
         for pos in self.world_map]
