"""Objektum renderelő szkriptje"""

import pygame as pg
import settings as s


class ObjectRenderer:
    """Objektum renderelőt reprezentáló osztály"""
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        """Fő rajzoló függvény, a render_game_objects
        munkáját itt hívjuk meg"""
        self.render_game_objects()

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
