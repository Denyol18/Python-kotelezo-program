"""Objektum renderelő szkriptje"""

import pygame as pg
import settings as s


class ObjectRenderer:
    """Objektum renderelőt reprezentáló osztály"""
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.ceiling_image = self.get_texture('resources/textures/ceiling.png',
                                              (s.WIDTH, s.HALF_HEIGHT))
        self.ceiling_offset = 0

    def draw(self):
        """Fő rajzoló függvény, a render_game_objects
        munkáját itt hívjuk meg"""
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        """Háttér rajzoló függvény"""

        # Plafon
        self.ceiling_offset = (self.ceiling_offset +
                               4.5 * self.game.player.rel) % s.WIDTH

        self.screen.blit(self.ceiling_image,
                         (-self.ceiling_offset, 0))

        self.screen.blit(self.ceiling_image,
                         (-self.ceiling_offset + s.WIDTH, 0))
        # Padló
        pg.draw.rect(self.screen, s.FLOOR_COLOR,
                     (0, s.HALF_HEIGHT, s.WIDTH, s.HEIGHT))

    def render_game_objects(self):
        """Megrajzolni kívánt objektumokat rajzoló függvény"""

        objects_list = self.game.raycasting.objects_to_render
        for depth, image, pos in objects_list:
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
            2: self.get_texture('resources/textures/2.jpg'),
            3: self.get_texture('resources/textures/3.jpg')
        }
