class Witch(object):

    def __init__(self):
        self.name = "Witch"
        self.health = 100
        self.strength = 11
        self.weapon = "Knife"
        self.house = "gingerbread"

    def get_health(self):
        return self.health

    def heal(self, recover):
        self.health = self.health + recover

    def harm(self, injury):
        self.health = self.health - injury

    def set_house(self, new_house):
        self.house = new_house

    def get_house(self):
        return self.house
