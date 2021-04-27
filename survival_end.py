from quit_story import Quit


class Scout(object):
    def __init__(self):
        pass

    @staticmethod
    def ending(self):
        print("You recall your many summers spent at camp tying knots.")
        print("Using your expertise, you manage to undo the knot using a Reverse-Cat's Cradle approach.")
        print("You always knew that knowing how to untie knots using only your pinkies would come in handy!")
        print("Before the witch can come back, you scoop up the kids and jump out of the nearest window before"
              " booking it as far into the woods as you can.")
        print("Safe from being eaten, all you have to do now is find your way home.")
        print("Too bad you don't have a compass.")
        Quit.quit_story(Quit)
