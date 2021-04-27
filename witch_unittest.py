import unittest
from witch_characteristics import Witch


class WitchTest(unittest.TestCase):

    def test_name(self):
        witch = Witch()
        self.assertEqual(witch.get_name(), "Witch")

    def test_house(self):
        witch = Witch()
        self.assertEqual(witch.get_house(), "gingerbread")
        witch.set_house("fudge")
        self.assertEqual(witch.get_house(), "fudge")


if __name__ == '__main__':
    unittest.main()
