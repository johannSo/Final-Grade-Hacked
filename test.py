import requests

url = "https://api.duckduckgo.com/?q=hello&format=json"
response = requests.get(url)
data = response.json()

print(data)
