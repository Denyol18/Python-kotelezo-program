"""Hangok scriptje"""

import pygame as pg


class Sound:
    """Hangot reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.machine_gun = pg.mixer.Sound(self.path + 'machine_gun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_shot.ogg')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')

        # Hangerő szabályzás

        self.machine_gun.set_volume(0.25)
        self.npc_pain.set_volume(0.5)
        self.npc_death.set_volume(0.25)
        self.npc_shot.set_volume(0.25)
        self.player_pain.set_volume(0.25)
