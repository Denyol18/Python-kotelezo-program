import pygame as pg
import math
import settings as s


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        pos_x, pos_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        ray_angle = self.game.player.angle - s.HALF_FOV + 0.0001
        for ray in range(s.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Vizszintes

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

            # Fuggoleges

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

            # Melyseg

            if vert_depth < hor_depth:
                depth = vert_depth
            else:
                depth = hor_depth

            # Rajzolas

            pg.draw.line(self.game.screen, 'white', (80 * pos_x, 80 * pos_y),
                         (80 * pos_x + 80 * depth * cos_a, 80 * pos_y + 80 * depth * sin_a), 2)

            ray_angle += s.DELTA_ANGLE

    def update(self):
        self.ray_cast()
