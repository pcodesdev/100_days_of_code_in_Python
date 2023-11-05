# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
age_as_int = int(age)
expected_lifespan_in_years = 90
remaining_years_to_live = expected_lifespan_in_years - age_as_int
days_remaining_to_live = remaining_years_to_live * 365
weeks_remaining_to_live = remaining_years_to_live * 52
months_remaining_to_live = remaining_years_to_live * 12

message = f"You have {days_remaining_to_live} days, {weeks_remaining_to_live} weeks, and {months_remaining_to_live} months left to live assuming\nthat you will die at 90 years old."
print(type(message))
print(message)








