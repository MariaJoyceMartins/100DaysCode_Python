# Conversion of thermometric scales


def start_screen():
    print(""""Welcome to the Thermometric scale calculator!"
    ------------------------------------------
    Available conversions:
    1. Celsius to Kelvin
    2. Kelvin to Celsius
    3. Fahrenheit to Celsius
    4. Celsius to Fahrenheit
    5. Fahrenheit to Kelvin
    6. Kelvin to Fahrenheit
    7. Exit
          """)


def get_temperature_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number: ")


def celsius_to_kelvin():
	celsius = get_temperature_input("Type the temperature in Celsius: ")
	kelvin = celsius + 273
	print(f"\n{celsius:.2f}°C = {kelvin:.2f}K\n")

def kelvin_to_celsius():
	kelvin = get_temperature_input("Type the temperature in Kelvin: ")
	celsius = kelvin - 273
	print(f"\n{kelvin:.2f}K = {celsius:.2f}°C\n")


def celsius_to_fahrenheit():
    celsius = get_temperature_input("Type the temperature in Celsius: ")
    fahrenheit = celsius * 1.8 + 32
    print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F\n")


def fahrenheit_to_celsius():
    fahrenheit = get_temperature_input("Type the temperature in Fahrenheit: ")
    celsius = (fahrenheit-32)/1.8
    print(f"\n{fahrenheit}°F = {celsius:.2f}°C\n")



def fahrenheit_to_kelvin():
    fahrenheit = get_temperature_input("Type the temperature in fahrenheit: ")
    kelvin =(fahrenheit-32) * 5/9 + 273
    print(f"\n{fahrenheit:.2f}°F = {kelvin:.2f}K\n")


def kelvin_to_fahrenheit():
    kelvin = get_temperature_input("Type the temperature in Kelvin: ")
    fahrenheit = (kelvin-273) * 1.8 + 32
    print(f"\n{kelvin:.2f}K = {fahrenheit:.2f}°F\n")

def main():
    while True:
        start_screen()
        choice = input("Choose a conversions (1-7): ")
        if choice == '1':
            celsius_to_kelvin()
        elif choice == '2':
            kelvin_to_celsius()
        elif choice == '3':
            fahrenheit_to_celsius()
        elif choice == '4':
           celsius_to_fahrenheit()
        elif choice == '5':
            fahrenheit_to_kelvin()
        elif choice == '6':
            kelvin_to_fahrenheit()
        elif choice == '7':
            print("Exiting program. GoodBye")
            break
        else:
            print("Invalid choice. Please select 1-7.")
        input("Press enter to continue...")

main()