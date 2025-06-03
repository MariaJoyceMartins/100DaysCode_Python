#Doing a game HangMan

import random
import requests

def fetch_random_word():
    respose = requests.get("https://random-word-api.herokuapp.com/word")
    return respose.json()[0]

random_word = fetch_random_word()
print(random_word)
