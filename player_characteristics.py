class Player(object):

    def __init__(self):

        self.name = ""
        self.health = 100
        self.strength = 10
        self.reason = ""
        self.weapon = "Unarmed"

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_reason(self, new_reason):
        self.reason = new_reason

    def get_reason(self):
        return self.reason

    def get_health(self):
        return self.health

    def heal(self, recover):
        self.health = self.health + recover

    def harm(self, injury):
        self.health = self.health - injury

    def add_weapon(self, weapon, item):
        self.strength = self.strength + item
        self.weapon = weapon
