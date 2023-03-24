"""
Jatek engine, ray casting megvalositasa
"""

import math
import pygame as pg
import settings as s


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        pos_x, pos_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        # Vizszintes

        # Fuggoleges

        ray_angle = self.game.player.angle - s.HALF_FOV + 0.0001
        for ray in range(s.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.sin(ray_angle)

            vert_x, inc_x = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)

            vert_depth = (vert_x - pos_x) / cos_a
            vert_y = pos_y + vert_depth * sin_a

            delta_depth = pos_x / cos_a
            pos_y = delta_depth * sin_a

            for i in range(s.MAX_DEPTH):
                vert_tile = int(vert_x), int(vert_y)
                if vert_tile in self.game.map.world_map:
                    break
                vert_x += pos_x
                vert_y += pos_y
                vert_depth += delta_depth

            ray_angle += s.DELTA_ANGLE

    def update(self):
        self.ray_cast()
