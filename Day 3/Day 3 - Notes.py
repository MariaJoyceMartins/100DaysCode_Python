# Challenge - To a Pizza Delivery Program

print("Welcome to Joy Pizza Deliveries!")
size = input("What size pizza do you want? (S, M or L): ")
pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ")
extra_cheese = input("Do you want extra cheese? (Y or N): ")

bill: int = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please, type a valid size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
else:
    bill += 3

if extra_cheese == "Y":
    bill += 1
else:
    bill == bill


if extra_cheese == "Y":
    bill += 1

print(f"You bill is: ${bill}")


###Logical Operators
# if condition 1 & condition 2 $ condition 3
# do this
# else:
# do this other thing

# A and B ---> all need to be true of false
# C or D
# not E

Maria
Joyce
Martins
Rabelo < maria.rabelo @ getninjas.com.br >

10: 35 PM(0
minutes
ago)

to
me
# In the python console, if we type
# a = 12
# a > 10 or a < 10
# The console will show: True

# Other case is:
# not a < 0
# The console will show: True
# not False
# The console will show: True
# not True
# The console will show: False

# Uptade the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that age is greather than 45, and it´s also less than 55

age = int(input("Type your age!"))
if age >= 45 and age <= 55:
    print("You can ride for free!")
else:
    print("You can´t ride por free")
