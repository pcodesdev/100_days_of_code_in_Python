
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill in Ksh?\n"))
tip_percent = int(input("how much tip would you like to give? 10, 12, 15?\n"))
number_of_people = int(input("How many people to split the bill?\n"))

total_amount_after_tip=total_bill+ (tip_percent/100*total_bill)

# First method on how to convert a number to two decimal places
# amount_to_pay_per_person = round((total_amount_after_tip / number_of_people), 2)

amount_to_pay_per_person = total_amount_after_tip / number_of_people

# The second method is:
# Convert to a string with 2 decimal places using f-string

message = f"Each person should pay Ksh: {amount_to_pay_per_person:.2f}"

print(total_amount_after_tip)

print(message)
#