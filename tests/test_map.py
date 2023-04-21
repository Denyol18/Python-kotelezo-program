"""map.py tesztelő szkriptje"""

import unittest
import python_kotelezo_program.main as main
import python_kotelezo_program.map as m


class TestMap(unittest.TestCase):
    """Tesztosztály a Map osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.map = m.Map(self.game, m.mini_map_1)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertTrue(self.map.game)     # Legyen értékük
        self.assertTrue(self.map.mini_map)
        self.assertTrue(self.map.world_map)
        self.assertFalse(self.map.get_map())  # Ne térjen vissza semmivel

    def test_draw(self):
        """A játékteret megrajzoló függvény tesztelése"""

        self.assertFalse(self.map.draw())  # Ne térjen vissza semmivel
