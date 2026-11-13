import random

door_open = False
in_castle = False
has_potion = False
outside_castle = False
number = 0
count = 0
moral = 0
itemcount = 0
player_health = 20
player_damage = 1
gold = 0



while count < 5:
    print('you take a step towards the castle')
    ##Roll for encounter
    ##if encounter is == to 4, fight goblin
    encounter = random.randint(1, 10)
    count = count + 1
    goblin_health = 3
    if encounter == 4:
        print("you encounter a goblin")
        while goblin_health > 0:
            goblin_attack = random.randint(1,3)
            player_health = player_health - goblin_attack
            combat = input("Would you like to attack or heal? a/h: ")
            ##each attack option hits the goblin
            if combat == 'a':
                print("You attack the goblin")
                goblin_health = goblin_health - player_damage
            ##Heal option during combat    
            if combat == 'h':
                print("you heal")
                player_health = player_health + 3
            
            print(f"your health: {player_health}")
            print(f"Goblin health: {goblin_health}")
            if goblin_health == 0:
                print("Goblin Defeated! +3 Gold")
                gold = gold + 3
            if player_health < 0:
                print("You Die!")
                break
           
print("you are outside the castle")
outside_castle = True
if player_health <= 0:
    outside_castle == False
while outside_castle == True:
    count = 0
    goblin_health = 3
    print("The castle is locked and needs a password")
    answer = input("What would you like to do? search or walk? ")
    if answer == 'walk':
        while count < 5:
            encounter = random.randint(1, 10)
            count = count +1
            if encounter == 4:
                print("you encounter a goblin")
                while goblin_health > 0:
                    goblin_attack = random.randint(1,3)
                    player_health = player_health - goblin_attack
                    combat = input("Would you like to attack or heal? a/h: ")
                    ##each attack option hits the goblin
                    if combat == 'a':
                        print("You attack the goblin")
                        goblin_health = goblin_health - player_damage
                    ##Heal option during combat    
                    if combat == 'h':
                        print("you heal")
                        player_health = player_health + 3
            
                    print(f"your health: {player_health}")
                    print(f"Goblin health: {goblin_health}")
                    if goblin_health < 0:
                        print("Goblin Defeated! +3 Gold")
                        gold = gold + 3
                        count = 0
                      
                    if player_health < 0:
                        print("You Died!")
                        break
    ##player will search for an item 1 -10            
##    if answer == 'search':
##        while count < 3:
##            count = count + 1
##            item = random.randint(1, 10)
##            if item == 1:
##                print("Holy Hand Grenade")
##            if item == 2:
##                
##            if item == 3:
##                
##            if item == 4:
##                
##            if item == 5:
##                
##            if item == 6:
##                
##            if item == 7:
##                
##            if item == 8:
##                
##            if item == 9:
##                
##            if item == 10:
                
        
while door_open == False:
    answer = input("Enter the password to open the door: ")
    if answer == 'Dragon':
        door_open = True
    else:
        print("Wrong password. Try again")
print("The door to the Castle opens. You enter.")
in_castle = True

while in_castle == True:
    answer = input("hello, I am the Good Wizard! Would you like to buy a spell? It's only 3 gold. y/n: ")
    if answer == 'y' and gold >= 3:
        print("Thank you have a good day! *He dissapears*")
        has_potion = True
        gold = gold -3
    if gold < 3:
        print("You do not have enough gold!")
    else:
        print("*He walks away sad*")
    break
    
    

