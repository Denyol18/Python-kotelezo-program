"""raycasting.py tesztelő szkriptje"""

import unittest
import python_kotelezo_program.main as main
import python_kotelezo_program.raycasting as r


class TestRayCasting(unittest.TestCase):
    """Tesztosztály a RayCasting osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.raycasting = r.RayCasting(self.game)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertTrue(self.raycasting.game)  # Legyen értéke
        self.assertFalse(self.raycasting.result)  # Legyenek üresek
        self.assertFalse(self.raycasting.objects_to_render)
        self.assertTrue(self.raycasting.textures)  # Legyen értéke

    def test_update(self):
        """Ray castinget frissítő függvény tesztelése"""

        self.assertFalse(self.raycasting.ray_cast())  # Ne térjenek vissza semmivel
        self.assertFalse(self.raycasting.get_objects_to_render())
