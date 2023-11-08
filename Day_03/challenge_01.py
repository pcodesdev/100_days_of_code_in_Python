# check if a given number is odd or even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests


# In computer programming, the "modulo" operation, often denoted by the symbol `%`, calculates the remainder of the division of one number by another. It's a mathematical operation that is frequently used in various programming tasks. The result of the modulo operation is the remainder that remains after one number is divided by another.
#
# Here's how the modulo operation works:
#
# Given two integers, `a` and `b`, the expression `a % b` returns the remainder when `a` is divided by `b`. In other words, it calculates how many times `b` can fit into `a`, and the result is the amount left over.
#
# For example:
#
# - `10 % 3` returns `1` because when you divide 10 by 3, you get a quotient of 3 and a remainder of 1.
# - `15 % 5` returns `0` because 15 is perfectly divisible by 5 with no remainder.
# - `-7 % 3` returns `2` because -7 divided by 3 gives a quotient of -2 and a remainder of 2.
#
# The modulo operation is commonly used in programming for various purposes, such as checking for even or odd numbers, cycling through arrays or lists, and implementing repeating patterns or periodic behavior. It's a versatile operation that can be found in many programming languages.

if number % 2 == 0:
  print("This number is Even")
else:
  print("This number is Odd")