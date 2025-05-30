# Functions
# Defining and Calling Python Functions

#In Python, have diferents functions defined, like:
print("Hello")

# All the functions pretty work the same, like por example:
num_char = len("Hello")
print(num_char)

# if we want to create or define a function, use:
def my_function():
    print("Hello")
    print("Bye")

#After this, calling your function for this be execute when you run

my_function()

# Now, we use the website "Reeborg World" with the objetive of practice function for make a robot walk, the code used was:

def robot_moviments():
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()

robot_moviments()

# Other possibility is:

def robot_moviments():
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()


robot_moviments()
turn_left()
move()
move()

# Challenge: Create a code that create a function to turn right the robot

def turn_right():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()

# Indentation - Is what have inside of the function
def my_function():
    print("Hello") # The indentation have this space for indicate that is inside the functiob
    print("World")

# Become more complicated when you have an indentation within an indentation
def drink_coffee():
    if coffee = "Empty":
        print("fill your cup")
    else:
        print("drink coffee")

drink_coffee()
