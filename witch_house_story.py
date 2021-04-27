from player_characteristics import Player
from witch_characteristics import Witch
from introduction import Introduction
from first_choice import First
from second_choice import Second
from third_choice import Third


class WitchHouse(object):
    def __init__(self, player: Player, witch: Witch):
        self.player = player
        self.witch = witch

    def play_game(self):
        Introduction.player_details(self.player, self.witch)
        First.first_choice(First)
        Second.second_choice(Second)
        Third.third_choice(Third)
