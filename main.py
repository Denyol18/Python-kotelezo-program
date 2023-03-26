"""Játék main scriptje, gerince"""

import sys
import pygame as pg
import map as m
import settings as s
import player as p
import raycasting as r
import object_renderer as o


class Game:
    """Magát a játékot reprezentáló osztály"""

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(s.RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.map = m.Map(self)
        self.player = p.Player(self)
        self.object_renderer = o.ObjectRenderer(self)
        self.raycasting = r.RayCasting(self)

    @staticmethod
    def check_events():
        """Billentyű kezelő statikus függvény"""
        for event in pg.event.get():
            if event.type == pg.QUIT or \
                    (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def update(self):
        """Ablakot megjelenítő, azt adatokkal folyamatosan ellátó függvény"""

        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(s.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        """Ablakot elemekkel feltöltő függvény"""

        # self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def run(self):
        """Játékot futtató függvény, mainben kell meghívni"""

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
