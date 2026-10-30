#guess the correct one

target  = 39
count = 0
while True :
    # target  = 39
    # count = 0
    num = int(input("guess : "))
    count+= 1

    if num > target :
        print("High")
    elif num < target :
        print("Low")
    else :
        print("Yahoo, correct guess")
        print("count: ",count)
        break

    # count+= 1