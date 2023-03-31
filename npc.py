"""NPCk scriptje"""

import sprite as sp
from random import randint, random, choice


class NPC(sp.AnimatedSprite):
    """NPCt reprezentáló osztály,
    ami az AnimatedSprite osztály gyerek osztálya"""

    def __init__(self, game, path='resources/sprites/'
                                  'npc/guard/0.png',
                 pos=(14.5, 7.5), scale=1, shift=0.36,
                 animation_time=180):

        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_image = self.get_images(self.path + '/death')
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
        self.get_sprites()
