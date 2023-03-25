"""
Jatek main scriptje
"""

import sys
import pygame as pg
import map as m
import settings as s
import player as p
import raycasting as r


def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(s.RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.map = m.Map(self)
        self.player = p.Player(self)
        self.raycasting = r.RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(s.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def run(self):
        while True:
            check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
