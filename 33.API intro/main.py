import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if response.status_code == 404:
#     raise Exception("Error")
# elif response.status_code == 401:
#     raise Exception("No permission.")

# does same thing as below 

response.raise_for_status()
data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(latitude,longitude)