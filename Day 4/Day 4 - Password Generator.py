import string
import random


# Password generator
def password_generator():
    size = int(input("Enter password length: "))
    password = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.sample(password, size))
    print(random_password)

password_generator()