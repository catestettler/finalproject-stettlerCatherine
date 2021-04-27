from witch_house_story import WitchHouse
from player_characteristics import Player
from witch_characteristics import Witch


if __name__ == '__main__':

    new_player = Player()
    new_witch = Witch()

    story = WitchHouse(new_player, new_witch)
    story.play_game()
