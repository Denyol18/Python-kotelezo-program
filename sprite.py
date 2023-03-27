"""Spriteok scriptje"""

import math
import pygame as pg
import settings as s


class Sprite:
    """Spriteot reprezentáló osztály"""

    def __init__(self, game, path='resources/sprites/'
                                  'static_sprites/barrel.png', pos=(9, 5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.screen_x = 0
        self.norm_dist = 1

    def get_sprite_projection(self):
        """Spriteok kivetítését lekérő függvény"""

        proj = s.SCREEN_DIST / self.norm_dist
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        sprite_half_width = proj_width // 2
        pos = self.screen_x - sprite_half_width, \
            s.HALF_HEIGHT - proj_height // 2

        self.game.raycasting.objects_to_render.append(
            (self.norm_dist, image, pos))

    def get_sprites(self):
        """Spriteokat lekérő függvény"""

        d_x = self.x - self.player.x
        d_y = self.y - self.player.y
        theta = math.atan2(d_y, d_x)
        delta = theta - self.player.angle

        if (d_x > 0 and self.player.angle > math.pi) or (d_x < 0 and d_y < 0):
            delta += math.tau

        delta_rays = delta / s.DELTA_ANGLE
        self.screen_x = (s.HALF_NUM_RAYS + delta_rays) * s.SCALE

        dist = math.hypot(d_x, d_y)
        self.norm_dist = dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < \
                (s.WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        """Spriteokat frissítő függvény"""

        self.get_sprites()