from ending_01 import Ending1


class First(object):
    def __init__(self):
        pass

    @staticmethod
    def first_end(self):
        Ending1.ending(Ending1)

    def first_choice(self):
        player_choice = input("Do you knock again? y/n")
        if player_choice == 'y':
            print("You knock again. This time, the door is opened by a small child.")
            print("You say hello, introduce yourself, and explain that you're lost.")
            print("Before the child can answer, you hear a raspy voice ask: 'Who is it?!'")
            print("The child tells the witch your name.")
            print("A rather decrepit old woman seems to just pop into existence behind the kid.")
            print("That's not creepy at all.")
            print("The woman scowls at you, her face vaguely resembling that of a saggy, rotten pumpkin.")
            print("'I don't know any .' they say. 'And can't you read the sign?!")
            print("They jab their finger at a sign hanging next to the door that reads:"
                  " NO SOLICITORS.")
            print("Weird. Where did that come from?")
            print("'Sorry to bother you, ma'am-'")
            print("'SIR.'")
            print("'Oh. Sorry.' Well now you feel awkward. 'Anyways, I'm lost and-'")
            print("'I don't care. Buzz off.'")
            print("The man is about to slam the door on you when you feel something tug on your leg.")
            print(
                "Glancing down, the small child has grabbed onto your pants and is looking up at you with pleading"
                " eyes.")
            print("Leaving doesn't seem like a great idea.")
        if player_choice == 'n':
            self.first_end(self)
