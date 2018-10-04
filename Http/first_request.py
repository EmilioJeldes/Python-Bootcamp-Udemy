import requests

url = "http://google.com"

res = requests.get(url)
print(f"Your request to {url} came back w/ status code {res.status_code}")

