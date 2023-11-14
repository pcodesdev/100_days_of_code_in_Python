# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(len(map))
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

print(position)

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# horizontal position
horizontal = int(position[0])
# vertical position
vertical = int(position[1])

# change the list element at the indicated position
map[horizontal -1][vertical - 1] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")