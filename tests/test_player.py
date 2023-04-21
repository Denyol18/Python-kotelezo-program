"""player.py tesztelő szkriptje"""

import unittest
import python_kotelezo_program.main as main
import python_kotelezo_program.player as p
import python_kotelezo_program.settings as s


class TestPlayer(unittest.TestCase):
    """Tesztosztály a Player osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.player = p.Player(self.game)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertTrue(self.player.game)
        self.assertEqual(self.player.angle, s.PLAYER_ANGLE, "Nem megfelelő érték!")
        self.assertFalse(self.player.rel)
        self.assertFalse(self.player.shot)
        self.assertEqual(self.player.health, s.PLAYER_MAX_HEALTH, "Nem megfelelő érték!")
        self.assertEqual(self.player.health_recovery_delay, 1000, "Nem megfelelő érték!")

    def test_update(self):
        """Player-t frissítő függvény tesztelése"""

        self.assertFalse(self.player.movement())   # Ne térjenek vissza semmivel
        self.assertFalse(self.player.mouse_control())
        self.assertFalse(self.player.recover_health())
        self.assertFalse(self.player.check_level_done())
