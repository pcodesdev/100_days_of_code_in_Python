#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

get_coin_face = random.randint(0,1)

if get_coin_face == 0:
    print("Tails")
else:
    print("Heads")

print(get_coin_face)