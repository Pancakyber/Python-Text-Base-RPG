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

print("----------------------------")
print("WELCOME TO THE FALL OF CORAK")
print("----------------------------")
print("y = yes | n = no | q = quit ")
print("h = help | i = inventory |  ")
print("l = location | north = north")
print("west = west | east = east   ")
print("south = south               ")
print("----------------------------")

while quitGame == False:
    gameStart = str(input("game started, would you like to quit?: ")).lower()
    if gameStart == 'y':
        quitGame == True
    elif gameStart == 'n':
        print("ok")
    else:
        print("not an input")
 
