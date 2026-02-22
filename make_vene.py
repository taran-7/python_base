import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(f"response.status_code: {response.status_code}")
print(f"response.json(): {response.json()}")
