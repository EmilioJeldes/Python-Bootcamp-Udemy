import requests

url = "https://icanhazdadjoke.com/search"
user_input = "cat"

res = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": user_input})

data = res.text

# print(data["results"][0]["joke"])
print(data)
