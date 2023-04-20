"""main.py tesztelő szkriptje"""

import unittest
import pygame as pg
import main
import map as m
import settings as s


class TestGame(unittest.TestCase):
    """Tesztosztály a Game osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.map = m.Map(self.game, m.mini_map_1)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertEqual(self.game.delta_time, 1, "Nem megfelelő érték!")
        self.assertEqual(self.game.levels_done, -1, "Nem megfelelő érték!")
        self.assertEqual(self.game.screen, pg.display.set_mode(s.RES), "Nem megfelelő érték!")

    def test_new_game(self):
        """Új játékot létrehozó függvény tesztelése"""

        self.assertEqual(self.game.npc_count, len(self.game.object_handler.npc_list),
                         "Nem megfelelő érték!")

    def test_draw(self):
        """Ablakba elemeket rajzoló függvény tesztelése"""

        self.assertFalse(self.game.object_renderer.draw())  # Ne térjen vissza semmivel
        self.assertFalse(self.game.weapon.draw())           # Ahogy ez se
