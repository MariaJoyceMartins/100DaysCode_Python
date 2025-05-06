# Seeing the types of each data
joy_beauty = True
my_money = 0.1 + 0.1
print(type(3864690244 + 462474))
print(type('lets do your best'))
print(type(joy_beauty))
print(type(my_money))

# Transforming data types - String to Integer
print(int("354") + int("1"))

# Transforming data types - Integer to String
name_len = len(input('Enter your name'))
print("Number of letter in your name: " + str(name_len))

# Mathematical Operations
print(3548 - 324)
print(4 * 5)
print(46/2) # the type data is float -> 2.0
print(46//2) # the type data is integer -> 2

# PEMDASLR
#
# ()
# **
# * OR /
# + OR -

# Change the result of this calculation, making the result 3 instead of 7

print(3 * 3 + 3 / 3 - 3)

# Calculation with result 3
print(3 * (3 + 3) / 3 - 3)

# Number Manipulation
bmi = 84 / 1.65 ** 2

# Transform to integer
print(int(bmi))

# Transform with round
print(round(bmi))

# Transform with round and choose the digits
print(round(bmi, 2))

# Uses scores a point
score = 10
score += 1
print(score)

# f-strings
print(f"Your score is equal to {score}")
