# Створення кортежу
coordinates = (10, 20)

my_address = ("вул. Лесі Українки", 15, "кв. 7", "Київ")

# Доступ такий самий, як у списку
print(coordinates[0])  # Виведе: 10

# Спроба змінити викличе помилку!
# coordinates[0] = 15  <-- Це зламає програму (TypeError)

# Додавання елемента до кортежу (створюється новий кортеж)
my_address_extended = my_address + ("Україна",)
print(my_address_extended)  # ('вул. Лесі Українки', 15, 'кв. 7', 'Київ', 'Україна')

print(f"Type of my_address_extended is: {type(my_address_extended)}")

# Перетворення рядка на кортеж
text = "Київ"
text_tuple = tuple(text)
print(text_tuple)  # ('К', 'и', 'ї', 'в')
