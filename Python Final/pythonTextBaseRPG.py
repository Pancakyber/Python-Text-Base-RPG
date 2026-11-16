#########################
#Game:                  #
#                       #
#Developed By Ryan Dydo #
#                       #
#Changelog: on github   # 
#                       #
#Version: Alpha 0.0.2   #
#########################
##Intilize Player Name and class
print("Before the games starts, what is your name?")
playerName = input("Enter Name: ")
 
##Import Random and Time
import time
import random
##Intialize Basic stuff
quitGame = True
newLocation = True
showMenu = True
##Initilize Player Stats
playerLevel = 1
playerHealth = 100
playerDamage = 10
gold = 0
karma = 50
xp = 0
#Classes
classless = True
archerClass = False
wizardClass = False
knightClass = False
##Initialize Items
wizardStaff = False
nobleSword = False
archersBow = False
heavyArmor = False
lightArmor = False
mediumArmor = False
##Item Stats (these are constants)
WIZARD_STAFF = 15
NOBLE_SWORD = 10
ARCHERS_BOW = 5
##Initialize Areas
inField = True
inFarm = False
inCave = False
inShop = False
inTavern = False
inWoods = False
inTown = False
inCastle = False
outsideCastle = False
#initilize functions
def levelUp():
    global playerLevel, playerHealth, playerDamage
##    print(f"level: {level}")
    playerLevel = playerLevel + 1
    playerHealth = playerHealth + 15
    playerDamage = playerDamage + 3
    print(f"+{playerLevel} lvl")
##initilize NPC
gobbyGoblinAlive = True
darkLordAlive = True
##Initilize NPC Health
gobbyGoblinHealth = 5
darkLordHealth = 150

if showMenu:
    print("----------------------------")
    print("WELCOME TO THE FALL OF CORAK")
    print("----------------------------")
    print("y = yes | n = no | q = quit ")
    print("h = help | i = inventory |  ")
    print("l = location | north = north")
    print("west = west | east = east   ")
    print("south = south | e = interact")
    print("f = fight |                 ")
    print("----------------------------")
    show_menu = False

while quitGame:

    while classless:
        print("""There are 3 classes to choose from
Archer
Wizard
Knight""")
        classSelection = str(input("Which class do you choose?: ")).lower()
        print()
        if classSelection == 'archer':
            archerClass = True
            archersBow = True
            heavyArmor = True
            playerDamage = playerDamage + ARCHERS_BOW
            classless = False
            
        elif classSelection == 'wizard':
            wizardClass = True
            wizardStaff = True
            lightArmor = True
            playerDamage = playerDamage + WIZARD_STAFF
            classless = False

        elif classSelection == 'knight':
            knightClass = True
            nobleSword = True
            mediumArmor = True
            playerDamage = playerDamage + NOBLE_SWORD
            classless = False
        else:
            print("not a real class")

        print(f"ah... so you are {playerName} the {classSelection}")
        print()
    ##Check if xp is greater than the playerLevel multiplied by 20 if it is reset xp and call the levelUp function
    if xp >= playerLevel * 20:
        xp = xp - playerLevel * 20
        levelUp()
    
    if newLocation:

        if inField:
            print("You wake up in a field otside of a city name Corak")
            print("The city lies to the north, but beware it is controlled by the dark lord.\n To the east lies the woods, it is full of peaceful creatures, but it may hold a powerful item! \n to the south is a cave where the goblin horde resides, they won't attack unless provoked! \n To the west is a small farm, perhaps you could get info there.") 

        elif inTown:
            print("in town")
        elif inCave:
            print("in cave")
            if gobbyGoblinAlive:
                print("You go into the goblin infested cave, and a small goblin aproaches you!")
                
           
            
        elif inWoods:
            print("in woods")
        elif inFarm:
            print("in farm")
        elif inTavern:
            print("in tavern")
        elif inShop:
            print("in shop")
        elif outsideCastle:
            print("outside castle")
        elif inCastle:
            print("in castle")

        newLocation = False

    direction = input("what would you to do?: ").lower()
    
    if direction == "north":
        
        inField = False
        inTown = True
        newLocation = True
    elif direction == "east":
        inField = False
        inWoods = True
        newLocation = True
    elif direction == "south":
        inField = False
        inCave = True
        newLocation = True
    elif direction == "west":
        inField = False
        inFarm = True
        newLocation = True
    elif direction == "q":
        quitGame = False
    elif direction == "h":
        showMenu = True
    elif direction == "i":
        print("----Inventory----")
        print("-----------------")
        if wizardStaff:
            print("Wizard Staff")
        if nobleSword:
            print("Noble Sword")
        if archersBow:
            print("Archer Bow")
        if lightArmor:
            print("Light Armor")
        if mediumArmor:
            print("Medium Armor")
        if heavyArmor:
            print("Heavy Armor")
    elif direction == 'e':
        if inCave and gobbyGoblinAlive:
            print("Hello I am gobby the goblin, do you have a gold coin I can borrow?")
    elif direction == 'f':
        if inCave and gobbyGoblinAlive:
            while gobbyGoblinHealth > 0:
                goblin_attack = random.randint(1,3)
                playerHealth = playerHealth - goblin_attack
                combat = input("Would you like to attack or heal? a/h: ")
            ##each attack option hits the goblin
                if combat == 'a':
                    print("You attack poor Gobby")
                    gobbyGoblinHealth = gobbyGoblinHealth - playerDamage
            ##Heal option during combat    
                if combat == 'h':
                    print("you heal")
                    playerHealth = playerHealth + 3
            
                print(f"your health: {playerHealth}")
                print(f"Gobby's health: {gobbyGoblinHealth}")
                if gobbyGoblinHealth <= 0:
                    print("Gobby was defeated! +3 Gold")
                    gold = gold + 3
                    karma = karma - 10
                    xp = xp + 20
                if playerHealth <= 0:
                    print("You Die!")
                    quitGame = False
                    
            
    
