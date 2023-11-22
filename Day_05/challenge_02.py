# 🚨 Don't change the code below 👇
# Use the split() method to split the user input string into a list of individual numbers
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    # converting inputs at their specific indexes to integers
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Initialize a variable to store the highest number: Set an initial value for the
# highest number, such as the first number in the list.
highest_score = student_scores[n]
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f'The highest score in the class is: {highest_score}')
