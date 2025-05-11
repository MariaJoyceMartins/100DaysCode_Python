import statistics

import numpy as np

# Calculate Average
def calculate_avg():
    user_input = input('Adicione os números para calcular a média: ')

    numbers_list = [num.strip() for num in user_input.split(',')]

    try:
        avg_numbers = [float(num) for num in numbers_list if num]
    except ValueError:
        print("Erro: é válido apenas números separados por uma virgula")
        exit()

    if not avg_numbers:
        print("Nenhum número digitado")
    else:
        average = sum(avg_numbers) / len(avg_numbers)
        print(f"A média é {average:.2f}")

calculate_avg()

# Calculate Mode
def calculate_mode():
    mode_user_input = input("Adicione os números para calcular a moda: ")

    mode_numbers_list = [num.strip() for num in mode_user_input.split(',')]

    try:
        mode_numbers = [float(num) for num in mode_numbers_list if num]
    except ValueError:
        print("Erro: é válido apenas numeros separados por uma virgula")
        exit()

    if not mode_numbers:
        print("Nenhum número digitado")
    else:
        mode = statistics.mode(mode_numbers)
        print(f"A moda é {mode}")

calculate_mode()

# Calculate Median
def calculate_median():
    median_user_input = input("Adicione os números para calcular a mediana: ")

    try:

        median_number = [float(num.strip()) for num in median_user_input.split(',') if num.strip()]
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 1, 2, 3.5)")
        return

    if not median_number:
        print("Erro: Nenhum número válido foi digitado")
        return

    median = statistics.median(median_number)
    print(f"A mediana é {median}")
calculate_median()

# Calculate Increase
def calculate_inc():
    print("Vamos calcular o aumento!\n")
    inc_old_value = int(input("Adicione o valor original: "))
    inc_new_value = int(input("Adicione o novo valor: "))
    increase = ((inc_new_value - inc_old_value) / inc_old_value) * 100
    print(f"O aumento foi de {increase:.2f}%")
calculate_inc()

# Calculate Decrease
def calculate_dec():
    print("Vamos calcular a diminuição!\n")
    dec_old_value = int(input("Adicione o valor original: "))
    dec_new_value = int(input("Adicione o novo valor: "))
    decrease = ((dec_new_value - dec_old_value) / dec_old_value) * 100
    print(f"A diminuição foi de {decrease:.2f}%")
calculate_dec()

# Calculate Max
def calculate_max():
    max_user_input = input("Adicione os números para calcular o maior: ")
    max_number_list = [num.strip() for num in max_user_input.split(',') if num.strip()]

    try:
        max_number = [int(num) for num in max_number_list]
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 1, 2, 3.5)")
        exit()

    if not max_number:
        print("Erro: Nenhum número válido foi digitado")
    else:
        maximum = max(max_number)
        print(f"O maior número é {maximum}")

calculate_max()

# Calculate Min
def calculate_min():
    min_user_input = input("Adicione os números para calcular o menor: ")

    min_number_list = [num.strip() for num in min_user_input.split(',') if num.strip()]

    try:
        min_number = [int(num) for num in min_number_list]
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 1, 2, 3.5)")
        return

    if not min_number:
        print("Erro: Nenhum número válido foi digitado")
    else:
        minimum = min(min_number)
        print(f"O menor número é {minimum}")

calculate_min()
