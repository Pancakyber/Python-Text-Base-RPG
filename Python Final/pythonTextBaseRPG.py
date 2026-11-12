#########################
#Game:                  #
#                       #
#Developed By Ryan Dydo #
#                       #
#Changelog: on github   # 
#                       #
#Version: Alpha 0.0.2   #
#########################
##Intilize Player Name
print("Before the games starts, what is your name?")
playerName = input("Enter Name: ")
##Import Random and Time
import time
import random
##Intialize Basic stuff
quitGame = False
##Initilize Player Stats
playerLevel = 1
playerHealth = 100
playerDamage = 10
gold = 0
#Classes
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
WIZARD_STAFF_DAMAGE = 15
NOBLE_SWORD = 10
ARCHERS_BOW = 5
##Initialize Areas

#initilize functions
def levelUp():
    global playerLevel
##    print(f"level: {level}")
    playerLevel = playerLevel + 1
    print(f"+{level} lvl")

print("----------------------------")
print("WELCOME TO THE FALL OF CORAK")
print("----------------------------")
print("y = yes | n = no | q = quit ")
print("h = help | i = inventory |  ")
print("l = location | north = north")
print("west = west | east = east   ")
print("south = south | e = interact")
print("----------------------------")

while quitGame != True:
    print("""There are 3 classes to choose from
Archer
Wizard
Knight""")
    classSelection = str(input("Which class do you choose?: ")).lower()
    if classSelection == 'archer':
        archerClass == True
        archersBow == True
        heavyArmor == True
    if classSelection == 'wizard':
        wizardClass == True
        wizardStaff == True
        lightArmor == True
    if classSelection == 'knight':
        knightClass == True
        nobleSword == True
        mediumArmor == True
    

    print(f"ah... so you are {playerName} the {classSelection}") 
    
