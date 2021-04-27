from quit_story import Quit


class Ending2(object):
    def __init__(self):
        pass

    @staticmethod
    def ending(self):
        print("You figure that this isn't really your problem. So you leave.")
        print("You heartless monster. I hope you're happy.")
        Quit.quit_story(Quit)
