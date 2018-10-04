import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

print(colored(figlet_format("DAD JOKE"), color = "magenta"))

url = "https://icanhazdadjoke.com/search"
user_input = input("What would you like to search for? ")

res = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": user_input})

data = res.json()["results"]

if not data:
    print("No results, please try again.")
else:
    print(f"{len(data)} results were found")
    print(choice(data)["joke"])
