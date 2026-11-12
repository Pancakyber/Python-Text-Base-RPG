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
    global playerLevel
##    print(f"level: {level}")
    playerLevel = playerLevel + 1
    print(f"+{level} lvl")
##ask class



    

if showMenu:
    print("----------------------------")
    print("WELCOME TO THE FALL OF CORAK")
    print("----------------------------")
    print("y = yes | n = no | q = quit ")
    print("h = help | i = inventory |  ")
    print("l = location | north = north")
    print("west = west | east = east   ")
    print("south = south | e = interact")
    print("----------------------------")
    show_menu = False

while quitGame:


    print("""There are 3 classes to choose from
Archer
Wizard
Knight""")
    classSelection = str(input("Which class do you choose?: ")).lower()
    if classSelection == 'archer':
        archerClass == True
        archersBow == True
        heavyArmor == True
        playerDamage = playerDamage + ARCHERS_BOW

    elif classSelection == 'wizard':
        wizardClass == True
        wizardStaff == True
        lightArmor == True
        playerDamage = playerDamage + WIZARD_STAFF

    elif classSelection == 'knight':
        knightClass == True
        nobleSword == True
        mediumArmor == True
        playerDamage = playerDamage + NOBLE_SWORD
    else:
        print("not a real class")

    print(f"ah... so you are {playerName} the {classSelection}")
    
    if newLocation:

        if inField:
            print("You wake up in a field otside of a city name Corak")
            print("The city lies to the north, but beware it is controlled by the dark lord.\n To the east lies the woods, it is full of peaceful creatures, but it may hold a powerful item! \n to the south is a cave where the goblin horde resides, they won't attack unless provoked! \n To the west is a small farm, perhaps you could get info there.") 

        elif inTown:
            print("in town")
        elif inCave:
            print("in cave")
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
        inField == False
        inTown == True
    elif direction == "east":
        inField == False
        inWoods == True
    elif direction == "south":
        inField == False
        inCave == True
    elif direction == "west":
        inField == False
        inFarm == True
    elif direction == "q":
        quitGame == False
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
            
    
