# goal: make a small game where I encounter multiple enemies
from pickle import TRUE
import random
import Lowlevelenemies

class Player:
    def __init__(self, health, damage):
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"You did {self.damage} to the enemy")
        return self.damage


class Goblin(Lowlevelenemies.Low_level_enemies):
    def __init__(self, health, original_health, damage):
        self.damage = damage
        self.health = health
        self.original_health = original_health

    def status(self):
        print(f"He has {self.health} health")
    
        

# label the goblins as entity numbers and create a loop of infinite battle cycling through.
axe_goblin = Goblin(50,50,10)
sword_goblin = Goblin(20, 20, 20)
grunt_goblin = Goblin(5, 5, 1)
Enemies = [axe_goblin,sword_goblin,grunt_goblin]
Enemies_name = ["axe goblin", "sword goblin", "grunt goblin"]
player1 = Player(100, 20)


while(player1.health>0):
    n = random.randint(0,len(Enemies)-1)
    print(f"You have encountered an {Enemies_name[n]}!")

    # find a way to make the game mechanic a class itself or in a class.
    while Enemies[n].health > 0:
        # player turn
        try:
            print('How do you want to proceed?: \n1:Attack \n2:Heal \n99:Suicide')
            player_turn = int(input())
        except ValueError:
            print("Invalid turn, you fumble")

        if player_turn == 1:
            Enemies[n].health = Enemies[n].health - player1.damage
            if(Enemies[n].health < 0):
                print("You have defeated the goblin") 
                Enemies[n].drops()
                Enemies[n].health = Enemies[n].original_health
                break
            print(f"The goblin has {Enemies[n].health} health left")
        elif player_turn == 2:
            player1.health += 50
            print("You healed 50 health")
        elif player_turn == 99:
            quit()
        else:
            print("Invalid turn, you fumble")
            
        # enemy turn
        player1.health = player1.health - Enemies[n].damage
        print(f"You take {Enemies[n].damage} damage") # a chance for critical hits?
            
        
