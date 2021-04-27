from ending_02 import Ending2


class Second(object):
    def __init__(self):
        pass

    @staticmethod
    def second_end(self):
        Ending2.ending(Ending2)

    def second_choice(self):
        player_choice = input("Do you stay? y/n")
        if player_choice == 'y':
            print("You hold the door open and almost force yourself into the house.")
            print("Look at you! Breaking and entering.")
            print("As you enter the house, your senses are almost overwhelmed by the smell of heavily seasoned food and"
                  " baked goods.")
            print("The house is also significantly bigger on the inside than you expected.")
            print("Looking around the room, you note a rather large oven and a...")
            input()
            print("A dog crate?")
            print("Holy Fresno, is that a kid in there?!")
            print("You feel something heavy hit you on the back of the head and everything goes black.")
            input()
            print("When you come to, you are tied to a chair.")
            print("You're not exactly sure why they tied you to a chair instead of throwing you in the crate, but"
                  " okay.")
            input()
            print("The child who opened the door for you is currently dragging a log the size of their body across the"
                  " room to place in the oven.")
            print("The other child has been put to work with a pair of bellows, fanning the flames of the large"
                  " cast-iron oven.")
            input()
            print("The old man - who you are now assuming is a witch - is leafing through a large, worn book,"
                  " and glancing up at you every few seconds.")
            print("Aw man. He's gonna eat you. Better think fast.")
        if player_choice == 'n':
            self.second_end(self)
