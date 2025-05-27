# Loops

# For Loops
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruits)
    print(fruit + "pie")
# In this case, the loop went through one item in the list and placed it in the output, and the code went through one of the fruits and placed it in the output. As it is a loop, it goes back and does the same with the next fruit, and so on.

# Calculate the sum highest score
student_scores = [150, 143, 185, 135, 150, 133, 109, 167, 159, 199, 171, 183, 154, 78, 69]
total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

# Challenge: Create the max highest score

student_score = [150, 139, 90]

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)


# Range Function
total = 0
for number in range(1, 101):
    total += number
print(total)