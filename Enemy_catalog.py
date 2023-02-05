import random


class Low_level_enemies:
    def __init__(self, health, original_health, damage, ailment=''):
        self.damage = damage
        self.health = health
        self.original_health = original_health
        self.ailment = ailment

    def status(self):
        print(f"He has {self.health} health")

    def status_ailment(self):
        if self.ailment == 'fire':
            self.health -= 1
        if self.ailment == 'disabled':
            self.damage /= 2
            

    def drops(self):
        loot = ["teeth", "scraps of leather", "sticks", "gold coins"]
        rand_loot_object = random.randint(0, len(loot)-1)
        rand_loot_num = random.randint(1, 5)
        if rand_loot_num == 1:  # fix the plurals
            switch = {
                0: "tooth",
                1: "scrap of leather",
                2: "a stick",
                3: "a gold coin"
            }
            switch.get(rand_loot_object, "oops")
        print(f"You find {rand_loot_num} {loot[rand_loot_object]}")


class Goblin(Low_level_enemies):
    def special_effect(self):
        if self.effect == 'fire':
            print('hi')


class Slime(Low_level_enemies):
    def special_effect(self):
        if self.effect == 'fire':
            print('hi')
