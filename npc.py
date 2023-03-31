"""NPCk scriptje"""

import settings as s
import sprite as sp
from random import randint, random, choice


class NPC(sp.AnimatedSprite):
    """NPCt reprezentáló osztály,
    ami az AnimatedSprite osztály gyerek osztálya"""

    def __init__(self, game, path='resources/sprites/'
                                  'npc/guard/0.png',
                 pos=(14.5, 7.5), scale=1, shift=0.1,
                 animation_time=180):

        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 6)
        self.speed = 0.002
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False

    def update(self):
        """NPCt frissítő függvény"""

        self.check_animation_time()
        self.get_sprite()
        self.run_logic()

    def animate_pain(self):
        """NPC sérülését animáló
        függvény"""

        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False

    def check_hit_in_npc(self):
        """NPCt való eltalálás vizsgáló
        függvény"""

        if self.game.player.shot:
            if s.HALF_WIDTH - self.sprite_half_width < self.screen_x \
                    < s.HALF_HEIGHT + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True

    def run_logic(self):
        """NPC mozgását megvalósító függvény"""

        if self.alive:
            self.check_hit_in_npc()
            if self.pain:
                self.animate_pain()
            else:
                self.animate(self.idle_images)
