# main.py

age: int = int(input("Enter your age: "))

if age < 13:
    print("You are a child :(")
elif 13 <= age <= 17:
    print("You are a teenager :-|")
elif 18 <= age <= 64:
    print("You are an adult :-)")
else:
    print("You are a Senior :-D")

# age: int = 27
# name: str = "Sasha"
# height: float = 1.75
# is_worker: bool = True

# print(f"Type the age is: {type(age)}\nType the name is: {type(name)}\nType the height is: {type(height)}\nType the is_worker is: {type(is_worker)}")

# print(f"Age: {age}, Name: {name}, Height: {height}, Is Worker: {is_worker}")

# name = input("Enter your name: ")
# age_str = input("Enter your age: ")
# height_str = input("Enter your height in meters (e.g. 1.75): ")

# age = int(age_str)
# height = float(height_str)

# print(f"Hello, {name}! You are {age} years old and {height} meters tall.")
