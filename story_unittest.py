import unittest
import witch_house_story


class MyTestCase(unittest.TestCase):
    def test_story(self):
        play = witch_house_story.Player()
        wit = witch_house_story.Witch()
        test_story = witch_house_story.WitchHouse(play, wit)
        witch_house_story.Introduction.player_details(play, wit)
        self.assertEqual(test_story.player.get_name(), "Bob")
        self.assertEqual(test_story.player.get_reason(), "berry picking")
        self.assertEqual(test_story.witch.get_name(), "Witch")
        self.assertEqual(test_story.witch.get_house(), "gingerbread")


if __name__ == '__main__':
    unittest.main()
