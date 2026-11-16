print("welcome to the game")
height = int(input("what is your height in cm "))
if height >= 130:
    print("welcome! you are eligible to play the game ")
    age = int(input("what is your age "))
    if age <= 12:
        bill = 0
        print("you cannot play")
    elif age <= 18:
        bill = 0
        print(" you still can't play")  
    else: 
        bill = 4
        print("congrats! you can now play successfully")   
    want_photo = int(input("do you want a photo while playing the game ? type y for yes and type n for no "))   
    if want_photo == "y":   
        bill = bill + 3
    print(f"yourtotal bill is {bill}")    
else:
    print("sry you can not play the game")        