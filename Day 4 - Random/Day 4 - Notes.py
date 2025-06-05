## Random Module

# to see more functions of the random library, go to https://docs.python.org/pt-br/3.13/library/random.html

import random as rd

# Random integral numbers
random_number = rd.randint(5, 10)
print(random_number)

# Random float numbers
random_float = rd.random()
print(random_float)

# Random uniform
# Definition: a <= N <= b, for a <= b
# and b <= N <= a for b < a
# Where N = float
random_uniform = rd.uniform(5,10)
print(random_uniform)

# Challenge - Heads os Tails
# Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" evemery it is runs
string = ["Heads", "Tails"]
random_string = rd.choice(string)
print(random_string)

## Lists
states_of_brazil = ["São Paulo", "Terra do Pão de Queijo", "Rio Grande do Sul", "Brasilia", "Rio de Janeiro"] #Have a order
print(states_of_brazil[2])

# It is also possible to use negative index, they will start from the last position of the list.
print(states_of_brazil[-1])

# For change the list with code
states_of_brazil[1] = "Minas Gerais"
print(states_of_brazil)

# For add to the list
states_of_brazil.append("Ceará")
print(states_of_brazil)

# to add multiple items to a list
states_of_brazil.extend(["Rio Grande do Norte", "Bahia", "Acré", "Roraima", "Amazonas", "Tocantins", "Santa Catarina", "Maranhão", "Pará"])
print(states_of_brazil)


# Challenge: Criar um sistema com que diz quem vai pagar a conta, sendo decidido de forma aleatoria

import random as rd

friends = ["Ana", "Beatriz", "Carla", "Dennis", "Esmeralda"]

random = rd.choice(friends)

print(random)