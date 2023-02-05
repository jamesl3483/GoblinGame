import random


class Weapons:
    def __init__(self, add_damage, ailment_chance, ailment=''):
        self.add_damage = add_damage
        self.ailment = ailment
        self.ailment_chance = ailment_chance
        

    def ailment_check(self):
        n = random.random()
        if n < 0.25:
            a = random.random()
            if a < .1:
                self.ailment = 'fire'
            a = random.random()
            if a < .1:
                self.ailment = 'iced'
            a = random.random()
            if a < .1:
                self.ailment = 'disabled'