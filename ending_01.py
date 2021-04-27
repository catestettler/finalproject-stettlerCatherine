from quit_story import Quit


class Ending1(object):
    def __init__(self):
        pass

    @staticmethod
    def ending(self):
        print("Welp. Guess this is a bust. Time to go wander around the forest and try to find"
              " your way home.")
        print("The end.")
        Quit.quit_story(Quit)
