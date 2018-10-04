import requests
from random import choice
import pyfiglet

print(pyfiglet.figlet_format("DAD JOKE"))

url = "https://icanhazdadjoke.com/search"
user_input = input("What would you like to search for? ")

res = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": user_input})

data = res.json()["results"]

if not data:
    print("No results, please try again.")
else:
    print(f"{len(data)} results were found")
    print(choice(data)["joke"])
