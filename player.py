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
        inc_x, inc_y = 0, 0
        speed = s.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            inc_x += speed_cos
            inc_y += speed_sin

        if keys[pg.K_s]:
            inc_x += -speed_cos
            inc_y += -speed_sin

        if keys[pg.K_a]:
            inc_x += speed_sin
            inc_y += -speed_cos

        if keys[pg.K_d]:
            inc_x += -speed_sin
            inc_y += speed_cos

        self.check_wall_collision(inc_x, inc_y)

        if keys[pg.K_LEFT]:
            self.angle -= s.PLAYER_ROT_SPEED * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle += s.PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, inc_x, inc_y):
        if self.check_wall(int(self.x + inc_x), int(self.y)):
            self.x += inc_x
        if self.check_wall(int(self.x), int(self.y + inc_y)):
            self.y += inc_y

    def draw(self):
        # pg.draw.line(self.game.screen, 'blue', (self.x * 80, self.y * 80),
        #             (self.x * 80 + s.WIDTH * math.cos(self.angle),
        #             self.y * 80 + s.WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'yellow',
                       (self.x * 80, self.y * 80), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
