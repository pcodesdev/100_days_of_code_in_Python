# control flow and logical operators


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Please get into the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("You will have to pay Ksh 500")
    elif age > 12 and age <=18:
        print("You will have to pay Ksh 700")
    else:
        print("You will have to pay Ksh 1200")
else:
    print("You are too short to get into the rollercoaster!")
