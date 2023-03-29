"""Játékos scriptje"""

import math
import pygame as pg
import settings as s


class Player:
    """Játékost reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.x, self.y = s.PLAYER_POS  # pylint: disable=invalid-name
        self.angle = s.PLAYER_ANGLE
        self.rel = 0

    def movement(self):
        """Játékos mozgásáért felelős függvény"""

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

        # if keys[pg.K_LEFT]:
        #    self.angle -= s.PLAYER_ROT_SPEED * self.game.delta_time

        # if keys[pg.K_RIGHT]:
        #    self.angle += s.PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def check_wall(self, x, y):  # pylint: disable=invalid-name
        """Falat detektáló függvény"""

        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, inc_x, inc_y):
        """Fallal való ütközés detektáló és kezelő függvény"""

        scale = s.PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + inc_x * scale), int(self.y)):
            self.x += inc_x
        if self.check_wall(int(self.x), int(self.y + inc_y * scale)):
            self.y += inc_y

    def draw(self):
        """Játékost reprezentáló kör és iránymutató
        vonal rajzoló függvény debugging célból"""

        # pg.draw.line(self.game.screen, 'blue', (self.x * 80, self.y * 80),
        #             (self.x * 80 + s.WIDTH * math.cos(self.angle),
        #             self.y * 80 + s.WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'yellow',
                       (self.x * 80, self.y * 80), 15)

    def mouse_control(self):
        """A játékos forgásáért felelős függvény"""

        m_x, m_y = pg.mouse.get_pos()
        if m_x < s.MOUSE_BORDER_LEFT or m_x > s.MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([s.HALF_WIDTH, s.HALF_HEIGHT])
        if m_y < s.MOUSE_BORDER_TOP or m_y > s.MOUSE_BORDER_BOTTOM:
            pg.mouse.set_pos([s.HALF_WIDTH, s.HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-s.MOUSE_MAX_REL, min(s.MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * s.MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        """Játékos frissítő függvény"""

        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        """Játékos koordinátáival visszatérő függvény"""

        return self.x, self.y

    @property
    def map_pos(self):
        """Függvény mely visszatér azzal a négyzettel,
        amelyiken a játékos éppen áll"""

        return int(self.x), int(self.y)
