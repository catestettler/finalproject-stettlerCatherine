import unittest
from player_characteristics import Player


class PlayerTest(unittest.TestCase):

    def test_name(self):
        player = Player()
        player.set_name("Bob")
        self.assertEqual(player.get_name(), "Bob")

    def test_reason(self):
        player = Player()
        player.set_reason("berry picking")
        self.assertEqual(player.get_reason(), "berry picking")


if __name__ == '__main__':
    unittest.main()
