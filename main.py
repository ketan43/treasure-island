print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#Write your code below this line 👇
answer_1 = input(
    'Okay quick, pick a direction, Beats chasing you down! Quick! "left" or "right"?: \n'
)

a1_lower = answer_1.lower()

if a1_lower == "right":
    print("You fell into the void, and disappeared. THE END")
elif a1_lower == "left":
    answer_2 = input(
        'Phew! Close call! Now you\'re at a river, "Swim" or "wait"? :  \n')
    a2_lower = answer_2.lower()
    if a2_lower == "swim":
        print("OH NO! The sea creatures caught you, sleep with the fishes!")
    elif a2_lower == "wait":
        print("Good call! A boat arrived, taking you closer to VICTORy!")
        answer_3 = input(
            "Okay you've arrived at 3 doors, pick one, Red, Yellow or Blue: \n"
        )
        a3_lower = answer_3.lower()
        if a3_lower == "red":
            print(
                "HORRIBLE! You fell into a flaming inferno, and got incinirated! AAARRRGHH!"
            )
        elif a3_lower == "blue":
            print(
                "Congratulations! You won the ULTIMATE treasure, yourself :)")
        elif a3_lower == "yellow":
            print("The giant in the room made you his pet, sorry!")
        else:
            print(
                "We asked you to pick a room and not be smart, GAME OVER, lame-o!"
            )

    else:
        print("You did something dumb, it's over!")

else:
    print(
        "You need to learn how to write, you've been sent back to pre-school")
