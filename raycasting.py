"""Játék engine, ray casting és kivetítés scriptje"""

import math
import pygame as pg
import settings as s


class RayCasting:
    """Ray castinget reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        """Megrajzolni kívánt objektumokat lekérő és tároló függvény"""

        self.objects_to_render = []
        for ray, values in enumerate(self.result):
            depth, proj_height, texture, offset = values

            if proj_height < s.HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (s.TEXTURE_SIZE - s.SCALE), 0,
                    s.SCALE, s.TEXTURE_SIZE
                )

                wall_column = pg.transform.scale(wall_column,
                                                 (s.SCALE, proj_height))

                wall_pos = (ray * s.SCALE, s.HALF_HEIGHT - proj_height // 2)
            else:
                texture_height = s.TEXTURE_SIZE * s.HEIGHT / proj_height

                wall_column = self.textures[texture].subsurface(
                    offset * (s.TEXTURE_SIZE - s.SCALE),
                    s.HALF_TEXTURE_SIZE - texture_height // 2,
                    s.SCALE, texture_height
                )

                wall_column = pg.transform.scale(wall_column,
                                                 (s.SCALE, s.HEIGHT))
                wall_pos = (ray * s.SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        """Ray castinget megvalósító függvény"""

        self.result = []
        pos_x, pos_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos
        hor_texture, vert_texture = 1, 1

        ray_angle = self.game.player.angle - s.HALF_FOV + 0.0001
        for ray in range(s.NUM_RAYS):  # pylint: disable=unused-variable
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Vízszintes irány

            hor_y, d_y = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
            hor_depth = (hor_y - pos_y) / sin_a
            hor_x = pos_x + hor_depth * cos_a

            delta_depth = d_y / sin_a
            d_x = delta_depth * cos_a

            for i in range(s.MAX_DEPTH):  # pylint: disable=unused-variable
                hor_tile = int(hor_x), int(hor_y)
                if hor_tile in self.game.map.world_map:
                    hor_texture = self.game.map.world_map[hor_tile]
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
                    vert_texture = self.game.map.world_map[vert_tile]
                    break
                vert_x += d_x
                vert_y += d_y
                vert_depth += delta_depth

            # Mélység, textúra beszámítás

            if vert_depth < hor_depth:
                depth, texture = vert_depth, vert_texture
                vert_y %= 1
                offset = vert_y if cos_a > 0 else (1 - vert_y)
            else:
                depth, texture = hor_depth, hor_texture
                hor_x %= 1
                offset = (1 - hor_x) if sin_a > 0 else hor_x

            # Fishbowl effect eltűntetése

            depth *= math.cos(self.game.player.angle - ray_angle)

            # Kivetítés

            proj_height = s.SCREEN_DIST / (depth + 0.0001)

            # Ray casting eredmény

            self.result.append((depth, proj_height, texture, offset))

            ray_angle += s.DELTA_ANGLE

    def update(self):
        """Ray castinget frissítő függvény"""

        self.ray_cast()
        self.get_objects_to_render()
