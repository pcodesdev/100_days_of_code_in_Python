# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆

total_sum = 0

for height in student_heights:
    total_sum += height

length = 0
for _ in student_heights:
    length += 1

average = round(total_sum / length)

print(total_sum)
print(average)
print(student_heights)

# method 2
# total_sum = 0
#
# for height in student_heights:
#     total_sum +=  height


# print(height)

# have completed challenge 1
