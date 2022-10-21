import random
import keyboard

hygeine = 5
health = 5
speed = 5
infected = False
job = 4                                 # Used to start while loop  
startMonth = 6                          # Used to start while loop
location = "Independence, Missouri"
day = 1
month = 0
year = 1848
oxenTotalCost = 0.00
foodTotalCost = 0.00
clothingTotalCost = 0.00
ammoTotalCost = 0.00
partsTotalCost = 0.00
totalCost = oxenTotalCost + foodTotalCost + clothingTotalCost + ammoTotalCost + partsTotalCost
#-----------------FUNCTIONS-------------------


def check4disease(hygeine, health, speed, infected):
    """Health check to determine if person should become sick/infected."""
    risk_of_infection = 10 - hygeine
    occurance_of_infection = random.randint(1,10)           # Determines chance of getting sick
    if (occurance_of_infection <= risk_of_infection):
        health -= 1
        speed -= 1
        infected = True 
        print("When you go to the bathroom, you discover dysentery. You are more susceptible to death and slower in travel. If you want to get better, you must be treated")
         
    else:
        print("Clean")
    return(health, speed, infected)


def integerCheck():
    """Restricts user to inputting integer values."""
    try:
        return int(input("\nWhat is your choice? "))
    except ValueError:
        print("\n\033[1;31m" + "Please choose one of the options" + "\033[0m")
        return integerCheck()


def inputCheck(numberOfOptions):
    """Restricts user to inputting value in given option range."""
    userInput = integerCheck()
    if numberOfOptions >= userInput > 0:
        return(userInput)
    else:
        print("\n\033[1;31m" + "Please choose one of the options" + "\033[0m")
        return inputCheck(numberOfOptions)


# Dialogue

while job == 4:                  # Loop repeats until user choses job
    print("\n-----------------------------------\
    \nMany kinds of people made the \
    \ntrip to Oregon. \
    \n\nYou may: \
    \n\n   1. Be a banker from Boston \
    \n   2. Be a carpenter from Ohio \
    \n   3. Be a gardner from Illinois \
    \n   4. Find out the differences \
    \n      between these choices")
    job = inputCheck(4)

    if job == 4:                # Job descriptions
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

if job == 1:                    # Starting money due to job choice
    money = 1600
elif job == 2:
    money = 800
elif job == 3:
    money = 400

name1 = input("\n-----------------------------------\
\nWhat is the first name of the \
\nwagon leader? ")              # User decides name of wagon leader

print(f"\n-----------------------------------\
\nWhat are the first names of the \
\nfour other members in your party? \
\n\n   1. {name1}")             # User decides names of party members
name2 = input("   2. ")
name3 = input("   3. ")
name4 = input("   4. ")
name5 = input("   5. ")

while startMonth == 6:           # User decides starting month
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
    startMonth = inputCheck(6)
    month = startMonth + 2
    if startMonth == 6:         # Starting month descriptions
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

print(f"\n-----------------------------------\
\nBefore leaving Independence you \
\nshould buy equipment and \
\nsupplies. You have ${money:.2f} in \
\ncash, but you don't have to \
\nspend it all now.")               # Scene setting dialogue
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')

print("\n-----------------------------------\
\nYou can buy whatever you need at \
\nMatt's General Store.")           # Scene setting dialogue
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')

print("\n-----------------------------------\
\nHello, I'm Matt. So you're going \
\nto Oregon! I can fix you up with \
\nwhat you need: \
\n\n       - a team of oxen to pull \
\n         your wagon \
\n       - clothing for both \
\n         summer and winter")      # Scene setting dialogue
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')

print("\n-----------------------------------\
\nHello, I'm Matt. So you're going \
\nto Oregon! I can fix you up with \
\nwhat you need: \
\n\n       - plenty of food for the \
\n         trip \
\n       - ammunition for your \
\n         rifles \
\n       - spare parts for your \
\n         wagon")                  # Scene setting dialogue
print("\n\033[1;32m" + "Press SPACE BAR to continue" + "\033[0m")
keyboard.wait('space')







# STORE SYSTEM

print(f"\n-----------------------------------\
\nMatt's General Store\
\n{location}\
\n\n{month} {day}, {year}\
\n-----------------------------------\
\n1. Oxen             ${oxenTotalCost:.2f}\
\n2. Food             ${foodTotalCost:.2f}\
\n3. Clothing         ${clothingTotalCost:.2f}\
\n4. Ammuntion        ${ammoTotalCost:.2f}\
\n5. Spare parts      ${partsTotalCost:.2f}\
\n-----------------------------------\
\nTotal bill:           ${totalCost:.2f}\
\n\nAmount you have:     ${money:.2f}")



print("\n-----------------------------------")
print(f"Matts General Store".center(35))
print(f"{location:^35}\n".center(35))
print(f"{month} {day}, {year}".center(35))
print(f"-----------------------------------")
print(f"1. Oxen             ${oxenTotalCost:.2f}".center(35))
print(f"2. Food             ${foodTotalCost:.2f}".center(35))
print(f"3. Clothing         ${clothingTotalCost:.2f}".center(35))
print(f"4. Ammuntion        ${ammoTotalCost:.2f}".center(35))
print(f"5. Spare parts      ${partsTotalCost:.2f}".center(35))
print("-----------------------------------")
print(f"Total bill:           ${totalCost:.2f}")
print(f"\nAmount you have:     ${money:.2f}")



#test
