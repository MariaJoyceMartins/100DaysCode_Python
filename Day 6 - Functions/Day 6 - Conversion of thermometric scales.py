# Conversion of thermometric scales

print("Welcome to the calculator that converts thermometric scales\n")

def celsius_to_kelvin():
	celsius = int(input("Type the temperature in Celsius: "))
	kelvin = celsius + 273
	print(f"The temperature in Kelvin is {kelvin}\n")
celsius_to_kelvin()

def kelvin_to_celsius():
	kelvin = int(input("Type the temperature in Kelvin: "))
	celsius = kelvin - 273
	print(f"The temperature in celsius is {celsius}\n")
kelvin_to_celsius()

def celsius_to_fahrenheit():
    celsius = int(input("Type the temperature in Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"The temperature in fahrenheit is {fahrenheit}\n")
celsius_to_fahrenheit()

def fahrenheit_to_celsius():
    fahrenheit = int(input("Type the temperature in Fahrenheit: "))
    celsius =(fahrenheit-32)/18
    print(f"The temperature in celsius is {celsius:.2f}\n")
fahrenheit_to_celsius()

def fahrenheit_to_kelvin():
    fahrenheit = int(input("Type the temperatue in fahrenheit: "))
    kelvin =(fahrenheit-32) * 5/9 + 273
    print(f"The temperature in kelvin is {kelvin:.2f}\n")
fahrenheit_to_kelvin()

def kelvin_to_fahrenheit():
    kelvin = int(input("Type the temperature in Kelvin: "))
    fahrenheit = (kelvin-273) * 1.8 + 32
    print(f"The temperature in fahrenheit is {fahrenheit:.2f}\n")
kelvin_to_fahrenheit()
