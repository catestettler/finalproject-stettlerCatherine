from ending_kids import Ending3
from branch import Branch


class Third(object):
    def __init__(self):
        pass

    @staticmethod
    def third_choice(self):
        print("You could try to convince the kids to help you. Or maybe you can buy yourself time to escape if you"
              " get the old man talking.")
        print("1. Appeal to the children")
        print("2. Distract the old man.")
        player_choice = input()
        if player_choice == '1':
            Ending3.ending(Ending3)
        if player_choice == '2':
            Branch.branching(Branch)
