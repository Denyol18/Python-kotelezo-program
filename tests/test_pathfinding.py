"""pathfinding.py tesztelő szkriptje"""

import unittest
import python_kotelezo_program.main as main
import python_kotelezo_program.pathfinding as pa


class TestPathFinding(unittest.TestCase):
    """Tesztosztály a PathFinding osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.pathfinding = pa.PathFinding(self.game)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertTrue(self.pathfinding.game)  # Legyen értékük
        self.assertTrue(self.pathfinding.game.map.mini_map)
        self.assertTrue(self.pathfinding.graph)
        self.assertFalse(self.pathfinding.get_graph())  # Ne térjen vissza semmivel
        self.assertFalse(self.pathfinding.visited)  # 0 == False

    def test_get_path(self):
        """Utat lekérő, annak végével visszatérő függvény tesztelése"""

        self.assertTrue(self.pathfinding.get_path((1, 1), (3, 3)))  # Térjen vissza vmi értékkel
