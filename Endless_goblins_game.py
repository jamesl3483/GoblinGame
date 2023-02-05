# goal: make a small game where I encounter multiple enemies
from pickle import TRUE
import random
import Enemy_catalog
import weapons_class

class Player(weapons_class.Weapons):
    def __init__(self, health, damage):
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"You did {self.damage} to the enemy")
        return self.damage
    
    def if_equip_weapon(self):
        self.damage += self.add_damage

enemies_list = {
    "Axe Goblin": Enemy_catalog.Goblin(50, 50, 10),
    "Sword Goblin": Enemy_catalog.Goblin(20, 20, 20),
    "Imp": Enemy_catalog.Goblin(5, 5, 1),
    "Fire Slime": Enemy_catalog.Slime(5,5,10, 'fire'),
    "Ice Slime": Enemy_catalog.Slime(5,5,5),
    "Poison Slime": Enemy_catalog.Slime(5,5,1)
}

Enemies = list(enemies_list.values())
Enemies_name = list(enemies_list.keys())
current_enemies = []
current_enemies_name = []


def battle_phase():
    def enemy_appearance():
        num_of_enemies = random.randint(1,3)
        for i in range(num_of_enemies):
            n = random.randint(0, len(Enemies)-1)
            print(f"You have encountered an {Enemies_name[n]}!")
            current_enemies.append(Enemies[n])
            current_enemies_name.append(Enemies_name[n])

    def choice_selection():
        try:
            print('You vs ', end='')
            for i in range(len(current_enemies)):
                print(f"{current_enemies_name[i]}, ", end='')
            print('\n')
            print('How do you want to proceed?: \n1:Attack \n2:Heal \n99:Suicide')
            return int(input())
        except ValueError:
            print("Invalid turn, you fumble")

    def enemy_selection():
        print("Select the enemy you want to attack")
        for i in range(len(current_enemies)):
            print(f"{i}: {current_enemies_name[i]}")
        return int(input())

    def attacking_enemy():
        enemy_attacked = enemy_selection()
        print(f"You deal {player1.damage} damage to {current_enemies_name[enemy_attacked]}")
        current_enemies[enemy_attacked].health -= player1.damage
        if(current_enemies[enemy_attacked].health <= 0):
            print(f"You have defeated the {current_enemies_name[enemy_attacked]}") 
            current_enemies[enemy_attacked].drops()
            current_enemies[enemy_attacked].health = current_enemies[enemy_attacked].original_health
            current_enemies.pop(enemy_attacked)
            current_enemies_name.pop(enemy_attacked)
        else:
            print(f"The goblin has {current_enemies[enemy_attacked].health} health left") 
        
    #     ailment_check(player1, current_enemies[enemy_attacked])  
            
    # def ailment_check(attacker, defender):
    #     if random.random() < attacker.ailment_chance:
    #         defender.status_ailment ### FIX, STOPPED HERE ###

    
    enemy_appearance()
    enemy_appearance()
    
    while len(current_enemies)>0:
        ########### player turn #################
        player_turn = choice_selection()
        if player_turn == 1:
            attacking_enemy()

        elif player_turn == 2:
            player1.health += 50
            print("You healed 50 health")
        elif player_turn == 99:
            quit()
        else:
            print("Invalid turn, you fumble")          
        
        ########### enemy turn #################
        for i in range(len(current_enemies)):
            player1.health -= current_enemies[i].damage
            print(f"{current_enemies_name[i]} deals {current_enemies[i].damage} damage") # a chance for critical hits?
            # print(f"{current_enemies[i].special_effect}")
            if player1.health<=0:
                print("You Died")
                quit()

        ########### random event #################
        chance_of_more_enemies = random.random()
        chance_of_more_loot = random.random()
        if  chance_of_more_enemies<0.2:
            enemy_appearance()
        elif chance_of_more_loot < 0.1:
            Enemy_catalog.Low_level_enemies.drops()


#main()   
player1 = Player(100, 20)  
while(player1.health>0):
    battle_phase()
