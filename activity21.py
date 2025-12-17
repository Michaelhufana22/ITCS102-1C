import random

print("Number Guessing Game")
print("==========================")

random_value =random.randint(1,3)
ulit = 0
resume = True

name = input("Please enter your name --> ")

while resume == True :
    num = eval(input("Guess a number from 1 to 10 "))
    ulit += 1
    if num == random_value :
        print("Winnerrr ka bihh!!")
        break
    else :
        print("Incorrect Guess")
        continue
        
print(f"HI {name}, Your guess is correct, number of ulit {ulit}")