class Witch(object):

    def __init__(self):
        self.name = "Witch"
        self.house = "gingerbread"

        """
        self.health = 100
        self.strength = 11
        self.weapon = "Knife"
        """
    def get_name(self):
        return self.name

    def set_house(self, new_house):
        self.house = new_house

    def get_house(self):
        return self.house

    """
    These are functions that I ran out of time to fully implement. There was going to be a feature in the game that
    would let you fight the witch (like a mini-game). I didn't get that implemented, so I just commented them out. I
    plan to go back and put them in later.
    
    def get_health(self):
        return self.health

    def heal(self, recover):
        self.health = self.health + recover

    def harm(self, injury):
        self.health = self.health - injury
        
    """
