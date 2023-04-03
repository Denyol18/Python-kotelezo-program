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
        self.blood_screen = self.get_texture('resources/textures/'
                                             'blood.png', s.RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/'
                                              f'digits/{i}.png',
                                              [self.digit_size] * 2)
                             for i in range(11)]

        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/'
                                                'game_over.png', s.RES)
        self.level_done_image = self.get_texture('resources/textures/'
                                                 'level_done.png', s.RES)

    def draw(self):
        """A rajzoló függvények együttesét
        képező függvény"""

        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def draw_player_health(self):
        """Játékos életerejét kirajzoló függvény"""

        i = 0
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))

        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        """Játékos sebződésekor rajzoló függvény"""

        self.screen.blit(self.blood_screen, (0, 0))

    def game_over(self):
        """Játék végén lévő képet rajzoló függvény"""

        self.screen.blit(self.game_over_image, (0, 0))

    def level_done(self):
        """Szint teljesítést követő képet rajzoló függvény"""

        self.screen.blit(self.level_done_image, (0, 0))

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

    def load_wall_textures(self):
        """Fall textúrákat betöltő függvény"""

        return {
            1: self.get_texture('resources/textures/1.jpg'),
            2: self.get_texture('resources/textures/1.jpg'),
            3: self.get_texture('resources/textures/1.jpg')
        }

    @staticmethod
    def get_texture(path, res=(s.TEXTURE_SIZE, s.TEXTURE_SIZE)):
        """Textúrát lekérő statikus függvény"""

        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
