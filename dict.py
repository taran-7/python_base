# # Створення словника
# user = {
#     "name": "Олексій",
#     "age": 25,
#     "city": "Київ"
# }

city = {
    "name": "Kyiv",
    "population": 3_500_000,
    "electrisity": "230V",
    "regions": ["Shevchenkivskyi", "Pecherskyi", "Podil", "Voskresenka"]
}

# Доступ до значення за ключем
# print(user["name"])  # Виведе: Олексій
print(city["regions"])

# # Додавання нової пари
# user["job"] = "Developer"
city["big"] = True


# # Зміна значення
# user["age"] = 26
city["population"] = 3_700_000

# print(user)
# # Виведе: {'name': 'Олексій', 'age': 26, 'city': 'Київ', 'job': 'Developer'}
print(f"Словник: {city}")
