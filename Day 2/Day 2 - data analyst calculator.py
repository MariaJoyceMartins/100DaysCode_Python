import statistics


# Calculate Average
def calculate_avg():
    print("Calculadora de Média")
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
        print(f"A média é {average:.2f}\n")

calculate_avg()

# Calculate Mode
def calculate_mode():
    print("\nCalculadora de Moda")
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
        print(f"A moda é {mode}\n")

calculate_mode()

# Calculate Median
def calculate_median():
    print("\nCalculadora de Mediana")
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
    print(f"A mediana é {median}\n")

calculate_median()

# Calculate Increase
def calculate_inc():
    print("\nCalculadora de Aumento")
    inc_old_value = float(input("Adicione o valor original: "))
    inc_new_value = float(input("Adicione o novo valor: "))
    increase = ((inc_new_value - inc_old_value) / inc_old_value) * 100
    print(f"O aumento foi de {increase:.2f}%\n")

calculate_inc()

# Calculate Decrease
def calculate_dec():
    print("\nCalculadora de Diminuição")
    dec_old_value = float(input("Adicione o valor original: "))
    dec_new_value = float(input("Adicione o novo valor: "))
    decrease = ((dec_old_value - dec_new_value) / dec_old_value) * 100
    print(f"A diminuição foi de {decrease:.2f}%\n")

calculate_dec()

# Calculate Max
def calculate_max():
    print("\nCalculadora de Valor Máximo")
    max_user_input = input("Adicione os números para calcular o maior: ")
    max_number_list = [num.strip() for num in max_user_input.split(',') if num.strip()]

    try:
        max_number = [float(num) for num in max_number_list]
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 1, 2, 3.5)")
        exit()

    if not max_number:
        print("Erro: Nenhum número válido foi digitado")
    else:
        maximum = max(max_number)
        print(f"O maior número é {maximum}\n")

calculate_max()

# Calculate Min
def calculate_min():
    print("\nCalculadora de Valor Minimo")
    min_user_input = input("Adicione os números para calcular o menor: ")
    min_number_list = [num.strip() for num in min_user_input.split(',') if num.strip()]

    try:
        min_number = [float(num) for num in min_number_list]
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 1, 2, 3.5)")
        return

    if not min_number:
        print("Erro: Nenhum número válido foi digitado")
    else:
        minimum = min(min_number)
        print(f"O menor número é {minimum}\n")

calculate_min()

# Calculate Conversation Rate
def calculate_conversation_rate():
    print("\nCalculadora de Taxa de Conversão")
    conversation = float(input("Digite o número de conversões: "))
    visitors = float(input("Digite o número de visitantes: "))
    conversation_rate = (conversation/visitors) * 100
    print(f"A taxa de conversão é de {conversation_rate:.2f}%\n")

calculate_conversation_rate()

# Calculate avg ticket
def calculate_avg_ticket():
    print("\nCalculadora de Ticket Médio")
    revenue = float(input("Digite o total de receita: "))
    transactions = float(input("Digite o total de transações: "))
    avg_ticket = revenue / transactions
    print(f"O ticket médio é {avg_ticket:.2f}\n")

calculate_avg_ticket()

# Calculate Churn Rate
def calculate_churn_rate():
    print("\nCalculadora de Churn Rate")
    lost_customers = float(input("Digite o total de clientes perdidos: "))
    total_customers = float(input("Digite o total de clientes: "))
    churn_rate = (lost_customers / total_customers) * 100
    print(f"O churn rate é {churn_rate:.2f}%\n")

calculate_churn_rate()

# Calculate CAC
def calculate_cac():
    print("\nCalculadora de CAC")
    expenses = float(input("Digite sua despesa total com Marketing e Vendas: "))
    customers = float(input("Digite a quantidade de clientes: "))
    cac = expenses / customers
    print(f"O valor do cac é {cac:.2f}\n")

calculate_cac()

