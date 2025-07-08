
# The graph to this game is in notes


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go:?")
crossroad = input("            Type L for Left and R for Right\n").lower()
if crossroad == 'l':
    print("You've reached an island. Do you want to wait for a boat or swim instead?")
    boat = input("       Type B for Boat or S for Swim\n").lower()
    if boat == 'b':
        print("Good! You've got on to the boat. there are three doors to choose from: Red, Purple and Blue")
        door = input("      Which door do you pick? Type R for Red, P for Purple and B for Blue\n").lower()
        if door == 'p':
            print("Congratulations!!You found the treasure... You WON the game!!")
        elif door == 'r':
            print("The room was on fire...Game Over!!")
        elif door == 'b':
            print("The room was filled with poisonous gas from plants...Game Over!!")
        else:
            print("You choose an invalid door...Game Over!!")
    elif boat == 's':
        print("You were swimming but an alligator got you..Game Over!!")
    else:
        print("You choose an invalid answer...Game Over!!")
elif crossroad == 'r':
    print("Oops! started with a wrong turn, you drowned in the sea... Game Over!!")
else:
    print("You choose an invalid answer...Game Over!!")