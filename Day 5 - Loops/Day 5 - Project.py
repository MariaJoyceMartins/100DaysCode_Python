# Check the minimum stock
from numpy.ma.core import minimum

total_stock = int(input("Please, enter the total stock: "))
minimum_stock = int(input("Please, enter the minimum stock: "))


def start_of_system():
    user_decide = input("Do you wanna to start the program? ")
    if user_decide == "yes":
        print("Welcome to your stock management system!")
    else:
        exit()

start_of_system()

def operations_system():
    stock_removed = int(input("Please, enter the stock to be removed: "))
    actually_stock = total_stock - stock_removed
    if actually_stock <= minimum_stock:
        print("You minimum stock is gone, buy more to make sure you don´t run out of anything")
    else:
        print(f"You have enough stock, being it {actually_stock}")


operations_system()



