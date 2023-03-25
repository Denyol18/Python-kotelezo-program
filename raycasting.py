"""
Játék engine, ray casting es kivetítés scriptje
"""

import math
import pygame as pg
import settings as s


class RayCasting:
    """Ray castinget reprezentáló osztály"""
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        """Ray castinget megvalosító függvény"""
        pos_x, pos_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        ray_angle = self.game.player.angle - s.HALF_FOV + 0.0001
        for ray in range(s.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Vízszintes irány

            hor_y, d_y = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
            hor_depth = (hor_y - pos_y) / sin_a
            hor_x = pos_x + hor_depth * cos_a

            delta_depth = d_y / sin_a
            d_x = delta_depth * cos_a

            for i in range(s.MAX_DEPTH):
                hor_tile = int(hor_x), int(hor_y)
                if hor_tile in self.game.map.world_map:
                    break
                hor_x += d_x
                hor_y += d_y
                hor_depth += delta_depth

            # Függőleges irány

            vert_x, d_x = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)
            vert_depth = (vert_x - pos_x) / cos_a
            vert_y = pos_y + vert_depth * sin_a

            delta_depth = d_x / cos_a
            d_y = delta_depth * sin_a

            for i in range(s.MAX_DEPTH):
                vert_tile = int(vert_x), int(vert_y)
                if vert_tile in self.game.map.world_map:
                    break
                vert_x += d_x
                vert_y += d_y
                vert_depth += delta_depth

            # Mélység

            if vert_depth < hor_depth:
                depth = vert_depth
            else:
                depth = hor_depth

            # Fishbowl effect eltűntetése

            depth *= math.cos(self.game.player.angle - ray_angle)

            # Kivetítés

            proj_height = s.SCREEN_DIST / (depth + 0.0001)

            # Fal rajzolás

            color = [255 / (1 + depth ** 5 * 0.005)] * 3
            pg.draw.rect(self.game.screen, color,
                         (ray * s.SCALE, s.HALF_HEIGHT - proj_height // 2,
                          s.SCALE, proj_height))

            ray_angle += s.DELTA_ANGLE

    def update(self):
        """Ray castinget frissítő függvény amit a Game osztályban hívunk meg"""
        self.ray_cast()
