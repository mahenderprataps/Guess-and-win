#guess the correct one

import random

target = random.randint(1, 100)
count = 0
while True :

    try :
        num = int(input("guess : "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    count+= 1

    if num > target :
        print("lower")
    elif num < target :
        print("higher")
    else :
        print("Yahoo, correct guess")
        print("count: ",count)
        break
