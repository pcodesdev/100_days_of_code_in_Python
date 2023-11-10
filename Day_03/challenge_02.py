# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height * height)

bmi_whole_num = round(bmi)

if bmi_whole_num <= 18.5:
    print(f"Your BMI is {bmi_whole_num} and you are \033[1munderweight\033[1m.")
elif bmi_whole_num <= 25:
    print(f"Your BMI is {bmi_whole_num} and you have \033[1mnormal weight\033[0m.")
elif bmi_whole_num <= 30:
    print(f"Your BMI is {bmi_whole_num} and you are \033[1mslightly overweight\033[0m.")
elif bmi_whole_num <= 35:
    print(f"Your BMI is {bmi_whole_num} and you are \033[1mobese\033[0m.")
# elif bmi_whole_num >=35:
else:
    print(f"Your BMI is {bmi_whole_num} and you are \033[1mclinically obese\033[1m.")
