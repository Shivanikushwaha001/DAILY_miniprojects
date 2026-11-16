import random

# what do you choose ? type 0 for rock , 1 for paper , or 2 for scissors.
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# here game_images is a list that contains the images of rock, paper, and scissirs.
game_images = [rock, paper, Scissors]
user_choice = int(input("what do you choose ? type 0 for rock , 1 for paper , oq 2 for scissors."))
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])
if user_choice  == 3 or user_choice <0:
    print("you typed an invalid number. you lose!")
elif user_choice == 3 or user_choice >2:
    print("you typed an invalid number.sorry! you lose.")    
elif user_choice == 0 and computer_choice == 2:
    print("you won..")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")    
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you won!")
else:
    print("its a  draw!")    
 