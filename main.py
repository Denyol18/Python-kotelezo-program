"""Játék main scriptje, gerince"""

import sys
import pygame as pg
import map as m
import settings as s
import player as p
import raycasting as r
import object_renderer as o
import object_handler as oh
import weapon as w
import sound as so
import pathfinding as pa


class Game:
    """Magát a játékot reprezentáló osztály"""

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(s.RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        """Új játékot létrehozó függvény"""

        self.map = m.Map(self, m.mini_map_1)
        self.player = p.Player(self)
        self.object_renderer = o.ObjectRenderer(self)
        self.raycasting = r.RayCasting(self)
        self.object_handler = oh.ObjectHandler(self)
        self.weapon = w.Weapon(self)
        self.sound = so.Sound(self)
        self.pathfinding = pa.PathFinding(self)

    def update(self):
        """Ablakot megjelenítő, azt adatokkal folyamatosan ellátó függvény"""

        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        self.sound.volume_control()
        pg.display.flip()
        self.delta_time = self.clock.tick(s.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        """Ablakba elemeket rajzoló függvény"""

        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        """Billentyű kezelő függvény"""

        for event in pg.event.get():
            if event.type == pg.QUIT or \
                    (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            self.player.single_fire_event(event)

    def run(self):
        """Játékot futtató függvény, mainben kell meghívni"""

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
