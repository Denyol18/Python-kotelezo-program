"""Objektum renderelő szkriptje"""

import pygame as pg
import settings as s


class ObjectRenderer:
    """Objektum renderelőt reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.jpg',
                                          (s.WIDTH, s.HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        """A rajzoló függvények együttesét
        képező függvény"""

        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        """Háttér rajzoló függvény"""

        # Égbolt
        self.sky_offset = (self.sky_offset +
                           4.5 * self.game.player.rel) % s.WIDTH

        self.screen.blit(self.sky_image,
                         (-self.sky_offset, 0))

        self.screen.blit(self.sky_image,
                         (-self.sky_offset + s.WIDTH, 0))
        # Padló
        pg.draw.rect(self.screen, s.FLOOR_COLOR,
                     (0, s.HALF_HEIGHT, s.WIDTH, s.HEIGHT))

    def render_game_objects(self):
        """Megrajzolni kívánt objektumokat rajzoló függvény"""

        objects_list = sorted(self.game.raycasting.objects_to_render,
                              key=lambda t: t[0], reverse=True)

        for depth, image, \
                pos in objects_list:  # pylint: disable=unused-variable

            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(s.TEXTURE_SIZE, s.TEXTURE_SIZE)):
        """Textúrát lekérő statikus függvény"""

        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        """Fall textúrákat betöltő függvény"""

        return {
            1: self.get_texture('resources/textures/1.jpg'),
            2: self.get_texture('resources/textures/1.jpg'),
            3: self.get_texture('resources/textures/1.jpg')
        }
