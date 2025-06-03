#Doing a game HangMan


#1 TO-DO: Create a random list of word
#2 TO-DO: Create a if/else logic of user when he wrong something
#3 TO-DO: Makes this run in a loop
#4 TO-DO: Define the total of things that the user can do
#5 TO-DO: Test if the code are work

#1 TO-DO:
import random
import requests

def fetch_random_word():
    respose = requests.get("https://random-word-api.herokuapp.com/word")
    return respose.json()[0]

random_word = fetch_random_word()
print(random_word)

#2 TO-DO:
input_letter = ("Try to define the word, for this, reply a letter")
if input_letter in random_word:
    input("You got one letter right!, Now that the next)
else:
    input("You got one letter wrong!, Now that the next")