
# main.py

# age: int = 27
# name: str = "Sasha"
# height: float = 1.75
# is_worker: bool = True

# print(f"Age: {age}, Name: {name}, Height: {height}, Is Worker: {is_worker}")

name = input("Enter your name: ")
age_str = input("Enter your age: ")
height_str = input("Enter your height in meters (e.g. 1.75): ")

age = int(age_str)
height = float(height_str)

print(f"Hello, {name}! You are {age} years old and {height} meters tall.")
