from survival_end import Scout
from ending_kids import Ending3
from culinary_end import Chef


class Branch(object):
    def __init__(self):
        pass

    @staticmethod
    def branch_end(self):
        print("1. Use your obscure survival skills to free yourself")
        print("2. Ask the kids to help you")
        player_choice = input()
        if player_choice == '1':
            Scout.ending(Scout)
        if player_choice == '2':
            Ending3.ending(Ending3)

    @staticmethod
    def branching(self):
        print("You casually ask the witch what he plans to do.")
        print("At least, you hope you sound casual.")
        print("The witch looks up at you, raising an eyebrow and asks if you have some input.")
        print("You do!")
        seasoning = input("What do you suggest?")
        print("The witch blinks. '", seasoning, "? Hadn't thought of that.'")
        print("'And how would you suggest doing that?'")
        input()
        print("You offer to show the witch, but he'll have to untie you.")
        print("He narrows his eyes. 'And how do I know you won't try anything funny?'")
        print("You hadn't thought this far ahead. What do you say?")
        print("1. I PINKY SWEAR.")
        print("2. I could stay tied to the chair, I guess.")
        player_choice = input()
        if player_choice == '1':
            print("'Can't argue with a pinky swear. But I mean it - no funny business!'")
            print("The witch unties you from the chair.")
            Chef.ending(Chef)
        if player_choice == '2':
            print("The witch seems satisfied with that, and gets up to grab a pen so he can take notes.")
            print("He leaves the kitchen, giving you a small window of opportunity to make your escape!")
            print("Better make it fast. What do you do?")
            self.branch_end(self)
