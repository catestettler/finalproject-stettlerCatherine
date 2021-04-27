from quit_story import Quit


class Chef(object):
    def __init__(self):
        pass

    @staticmethod
    def ending(self):
        print("True to your word, you demonstrate for the witch using some meat that they happened to have"
              " on hand.")
        print("The witch is enthralled by your display. He is so impressed and in awe, that he decides it"
              " would be a waste to kill you.")
        print("You tell him that you'd be more than happy to share more tips with him if he lets you and "
              "the kids leave.")
        print("He agrees. And you leave the house without any bloodshed.")
        print("Looks like you've made yourself a dubious new friend! Good for you!")
        Quit.quit_story(Quit)
