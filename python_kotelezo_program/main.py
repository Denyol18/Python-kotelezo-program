"""Játék main scriptje, gerince"""

import sys
import pygame as pg
import python_kotelezo_program.map as m
import python_kotelezo_program.settings as s
import python_kotelezo_program.player as p
import python_kotelezo_program.raycasting as r
import python_kotelezo_program.object_renderer as o
import python_kotelezo_program.object_handler as oh
import python_kotelezo_program.weapon as w
import python_kotelezo_program.sound as so
import python_kotelezo_program.pathfinding as pa


class Game:
    """Magát a játékot reprezentáló osztály"""

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(s.RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.levels_done = -1
        self.new_game(m.mini_map_1)

    def new_game(self, mini_map):
        """Új játékot létrehozó függvény"""

        self.map = m.Map(self, mini_map)
        self.player = p.Player(self)
        self.object_renderer = o.ObjectRenderer(self)
        self.raycasting = r.RayCasting(self)
        self.object_handler = oh.ObjectHandler(self)
        self.weapon = w.Weapon(self)
        self.sound = so.Sound(self)
        self.pathfinding = pa.PathFinding(self)
        self.npc_count = len(self.object_handler.npc_list)

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
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            self.player.single_fire_event(event)

    def run(self):
        """Játékot futtató függvény"""

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
