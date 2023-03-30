"""Hangkezelő scriptje"""

import pygame as pg


class Sound:
    """Hangot reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.machine_gun = pg.mixer.Sound(self.path + 'machine_gun.wav')
