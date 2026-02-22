import requests

response = requests.get("https://www.ukr.net/ajax/start.json")
print(response.status_code)
print(f"response.status_code: {response.status_code}")
print(f"response.json(): {response.json()}")
