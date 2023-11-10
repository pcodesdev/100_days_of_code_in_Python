# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# The key points are:
#
# A year is a leap year if it is divisible by 4
# Except if it is divisible by 100, then it isn't
# Unless it is also divisible by 400, then it is
# So the steps are:
#
# Check if the year is divisible by 4
# If yes, go to next step
# If no, return False - not a leap year
# Check if year is divisible by 100
# If yes, go to next step
# If no, return True - it is a leap year
# Check if year is divisible by 400
# If yes, return True - it is a leap year
# If no, return False - not a leap year
# This will correctly determine if a given year is a leap year in Python.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")

