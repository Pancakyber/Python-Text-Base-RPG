#########################
#Game:                  #
#                       #
#Developed By Ryan Dydo #
#                       #
#Changelog:             # 
#                       #
#Version: Alpha 0.0.1   #
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
playerDamage = 10
gold = 0
##Initialize Items
wizardStaff = False
print("---------------------------")
print("WELCOME TO WIZARD ADVENTURE")
print("---------------------------")
while quitGame == False:
    gameStart = str(input("game started, would you like to quit?: ")).lower()
    if gameStart == 'y':
        quitGame == True
    elif gameStart == 'n':
        print("ok")
    else:
        print("not an input")
 
