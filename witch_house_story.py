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
        self.first = First()
        self.sec = Second()
        self.third = Third()

    def play_game(self):
        Introduction.player_details(self.player, self.witch)
        self.first.first_choice()
        self.sec.second_choice()
        self.third.third_choice(self.third)
