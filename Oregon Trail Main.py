import random
from this import d
import keyboard

#--------------VARIABLES--------------
name = 'steve'  #this is here in order to create global variable
marital = False     
children = 0   
transportation = 'foot'
religion = 0
security = 0
infected = False
year = 1848
population = 10000 * random.randint(30, 40)
weather = 0 #0 is sunny, 1 is rainy, 2 is thunderstorm, 3 is snow storm
cash = 0
oxen = 0
warmth = 0
distance = 0
hygeine = 5
health = 5
speed = 5

#-----------------FUNCTIONS-------------------
def check4disease(hygeine, newHealth, newSpeed, newInfected):
    """Health check to determine if person should become sick/infected"""
    risk_of_infection = 10 - hygeine
    occurance_of_infection = random.randint(1,10)           #Determines chance of getting sick
    if (occurance_of_infection <= risk_of_infection):
        newHealth -= 1
        newSpeed -= 1
        newInfected = True 
        print("When you go to the bathroom, you discover dysentery. You are more susceptible to death and slower in travel. If you want to get better, you must be treated")
         
    else:
        print("Clean")
    return(newHealth, newSpeed, newInfected)

# health, speed, infected = check4disease(hygeine, health, speed, infected) ------ when calling it


time = 1        #every number is six hours: goes from 1 (6 am) to * 4 (12 am) time % 4 == 1, 2, 3, 0 signals time
#create function that converts time to hour every time it is called upon





#----------------family names are in list-----


#------------format of inputs-------------


#Dialogue

job = 10                        #Used to start while loop  
startMonth = 13                 #Used to start while loop

while job > 3:                  #Loop repeats until user choses job
    print("\n-----------------------------------\
    \nMany kinds of people made the \
    \ntrip to Oregon. \
    \n\nYou may: \
    \n\n   1. Be a banker from Boston \
    \n   2. Be a carpenter from Ohio \
    \n   3. Be a garmer from Illionois \
    \n   4. Find out the differences \
    \n      between these choices")
    job = int(input("\nWhat is your choice? "))

    if job == 4:                #Job descriptions
        print("\n-----------------------------------\
        \nTraveling to Oregon isn't easy! \
        \nBut if you're a banker, you'll \
        \nhave more money for supplies \
        \nand services than a carpenter \
        \nor a farmer. \
        \n\nHowever, the harder you have \
        \nto try, the more points you \
        \ndeserve! Therefore, the \
        \nfarmer earns the greatest \
        \nnumber of points and the \
        \nbanker earns the least.") 
        print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
        keyboard.wait('space')
    elif job > 4:               #Gives error if user inserts a non-option
        print("\n-----------------------------------\
        \n\033[1;31m" + "Please choose one of the options." + "\033[0m")
        print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
        keyboard.wait('space')


if job == 1:                    #Starting money due to job choice
    money = 1600
elif job == 2:
    money = 800
elif job == 3:
    money = 400


name1 = input("\n-----------------------------------\
\nWhat is the first name of the \
\nwagon leader? ")              #User decides name of wagon leader
print(f"\n-----------------------------------\
\nWhat are the first names of the \
\nfour other members in your party? \
\n\n   1. {name1}")
name2 = input("   2. ")
name3 = input("   3. ")
name4 = input("   4. ")
name5 = input("   5. ")
while startMonth > 5:           #User decides names of party members
    print("\n-----------------------------------\
    \nIt is 1848. Your jumping off \
    \nplace for Oregon is Independence, \
    \nMissouri. You must decide which \
    \nmonth to leave Independence. \
    \n\n   1. March \
    \n   2. April \
    \n   3. May \
    \n   4. June \
    \n   5. July \
    \n   6. Ask for advice")
    startMonth = int(input("\nWhat is your choice? "))

    if startMonth == 6:         #Starting month descriptions
        print("\n-----------------------------------\
        \nYou attend a public meeting held \
        \nfor \"folks with the California - \
        \nOregon fever.\" You're told: \
        \n\nIf you leave too early, there \
        \nwon't be any grass for your \
        \noxen to eat. If you leave too \
        \nlate, you may not get to Oregon \
        \nbefore winter comes. If you \
        \nleave at just the right time, \
        \nthere will be green grass and \
        \nweather will still be cool.")
        print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
        keyboard.wait('space')
    elif startMonth > 6:        #Gives error if user inserts a non-option
        print("\n-----------------------------------\
        \n\033[1;31m" + "Please choose one of the options." + "\033[0m")
        print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
        keyboard.wait('space')


print(f"\n-----------------------------------\
\nBefore leaving Independence you \
\nshould buy equipment and \
\nsupplies. You have ${money:.2f} in \
\ncash, but you don't have to \
\nspend it all now.")
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')
print("\n-----------------------------------\
\nYou can buy whatever you need at \
\nMatt's General Store.")
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')