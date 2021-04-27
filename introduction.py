from player_characteristics import Player
from witch_characteristics import Witch


class Introduction(object):
    def __init__(self):
        pass

    @staticmethod
    def player_details(player: Player, witch: Witch):
        player_name = input("Please enter your name:")
        player.set_name(player_name)
        print("Welcome", player.get_name(), "! ")
        print("As with all good stories, we start in some creepy forest "
              "(Likely somewhere in Germany).")
        player_reason = input("Why are you in the forest?")
        player.set_reason(player_reason)
        print("Really? Okay. Not the weirdest thing I've heard today.")
        print("Anyways, you are in the forest because", player.get_reason(),
              ", and have come to find yourself in a clearing.")
        print("At the middle of this clearing is a house made of...")
        witch_house = input("What is the house made of?")
        witch.set_house(witch_house)
        print("A house made of", witch.get_house(), ". Again, not the weirdest thing today.")
        print("You approach the house and knock on the door.")
        print("No one answers.")
