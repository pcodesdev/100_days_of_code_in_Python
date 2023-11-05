# BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#calculate BMI
# convert both the height and weight into floats
height_float = float(height)
weight_float = float(weight)
BMI = weight_float / (height_float ** height_float)
# convert the whole solution into an integer
results = int(BMI)
print(results)
