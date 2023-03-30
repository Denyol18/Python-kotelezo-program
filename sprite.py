"""Spriteok scriptje"""

import os
import math
from collections import deque
import pygame as pg
import settings as s


class Sprite:
    """Spriteot reprezentáló osztály"""

    def __init__(self, game, path='resources/sprites/'
                                  'static_sprites/barrel.png', pos=(9.8, 5),
                 scale=0.5, shift=0.5):

        self.game = game
        self.player = game.player
        self.x, self.y = pos  # pylint: disable=invalid-name
        self.image = pg.image.load(path).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_half_width = self.image.get_width() // 2
        self.image_ratio = self.image_width / self.image.get_height()
        self.screen_x = 0
        self.norm_dist = 1
        self.sprite_scale = scale
        self.sprite_height_shift = shift

    def get_sprite_projection(self):
        """Spriteok kivetítését lekérő függvény"""

        proj = s.SCREEN_DIST / self.norm_dist * self.sprite_scale
        proj_width, proj_height = proj * self.image_ratio, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        sprite_half_width = proj_width // 2

        height_shift = proj_height * self.sprite_height_shift

        pos = self.screen_x - sprite_half_width, \
            s.HALF_HEIGHT - proj_height // 2 + height_shift

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
        if -self.image_half_width < self.screen_x < \
                (s.WIDTH + self.image_half_width) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        """Spriteokat frissítő függvény"""

        self.get_sprites()


class AnimatedSprite(Sprite):
    """Animált spriteot reprezentáló osztály,
    ami a Sprite osztály gyerek osztálya"""

    def __init__(self, game, path='rescources/sprites/'
                                  'animated_sprites', pos=(5, 5),
                 scale=0.5, shift=0.5, animation_time=120):

        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        """Animált spriteokat frissítő függvény"""

        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        """Animáció lejátszó függvény"""

        if self.animation_trigger:
            images.rotate(-1)
            self.images = images[0]

    def check_animation_time(self):
        """Animáció idő figyelő függvény"""

        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    @staticmethod
    def get_images(path):
        """Képeket lekérő és tároló függvény"""

        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images
