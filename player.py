"""
Jatekos beallitasok
"""

import math
import pygame as pg
import settings as s


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = s.PLAYER_POS
        self.angle = s.PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = s.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos

        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        if keys[pg.K_LEFT]:
            self.angle -= s.PLAYER_ROT_SPEED * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle += s.PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'blue', (self.x * 40, self.y * 40),
                     (self.x * 40 + s.WIDTH * math.cos(self.angle),
                     self.y * 40 + s.WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'yellow', (self.x * 40, self.y * 40), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
