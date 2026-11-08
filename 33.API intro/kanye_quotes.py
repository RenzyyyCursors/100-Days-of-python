import requests

response = requests.get("https://api.kanye.rest")

print(response.json()['quote'])