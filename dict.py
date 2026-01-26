import sys

# Створення словника
user = {
    "name": "Олексій",
    "age": 25,
    "city": "Київ"
}

# Доступ до значення за ключем
print(user["name"])  # Виведе: Олексій

# Додавання нової пари
user["job"] = "Developer"

# Зміна значення
user["age"] = 26

print(user)
# Виведе: {'name': 'Олексій', 'age': 26, 'city': 'Київ', 'job': 'Developer'}
