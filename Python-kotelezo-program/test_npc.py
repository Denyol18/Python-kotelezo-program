"""npc.py tesztelő szkriptje"""

import unittest
import main
import npc


class TestNPC(unittest.TestCase):
    """Tesztosztály az NPC osztály tesztelésére"""

    def setUp(self):
        self.game = main.Game()
        self.npc = npc.NPC(self.game)

    def test_init(self):
        """Konstruktor tesztelő függvény"""

        self.assertTrue(self.npc.game)  # Legyen értéke
        self.assertEqual(self.npc.speed, 0.02, "Nem megfelelő érték!")
        self.assertEqual(self.npc.size, 10, "Nem megfelelő érték!")
        self.assertEqual(self.npc.health, 100, "Nem megfelelő érték!")
        self.assertEqual(self.npc.attack_damage, 10, "Nem megfelelő érték!")
        self.assertEqual(self.npc.accuracy, 0.25, "Nem megfelelő érték!")
        self.assertTrue(self.npc.alive)  # Legyen értékük
        self.assertFalse(self.npc.pain)
        self.assertFalse(self.npc.ray_cast_value)
        self.assertFalse(self.npc.frame_counter)  # 0 == False
        self.assertFalse(self.npc.player_search_trigger)

    def test_update(self):
        """NPCt frissítő függvény tesztelése"""

        self.assertFalse(self.npc.check_animation_time())  # Ne térjenek vissza semmivel
        self.assertFalse(self.npc.get_sprite())
        self.assertFalse(self.npc.run_logic())
