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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("welcome to the treasure island.")
print("your aim is to find the treasure..")
choice1 = input('you\'v entered the game!,where do you want to go? type "left"  or type "right".' ).lower()
if choice1 == "left":
    choice2 = input('you\'ve came to a lake, there is a island also in the midlle' \
    ' of the lake. type "wait" if you want to wait f0r the boat. type "swim" if you want to swim').lower()
    if choice2 =="wait":
        choice3 = input("you have successfully arrived the island." \
        "there is a house with further three doors.one is red. one is yellow ."
        "the another one is blue").lower()

# you have entered the game 
    
        
        if choice3 == "red":
            print("the room is full of fire! game over. ")
        elif choice3 == "yellow":
            print("congrats! you'v found the treasure.")
        elif choice3 == "blue":
            print("better luck next time..")
        else: 
            print("you'v not chossen invalid option.") 
else:   
    print("sorry! you lose the game.")