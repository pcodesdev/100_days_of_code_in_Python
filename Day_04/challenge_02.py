# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# get the random index of the names received by names_string variable
random_index = random.randint(0, len(names) -1)

# print a random name
print(f"{names[random_index]} is going to buy the meal today!")


