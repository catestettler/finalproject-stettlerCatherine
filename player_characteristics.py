class Player(object):

    def __init__(self):

        self.name = "Bob"
        self.reason = "berry picking"

        """
        self.health = 100
        self.strength = 10
        self.weapon = "Unarmed"
        """

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_reason(self, new_reason):
        self.reason = new_reason

    def get_reason(self):
        return self.reason

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

    def add_weapon(self, weapon, item):
        self.strength = self.strength + item
        self.weapon = weapon
        
    """
