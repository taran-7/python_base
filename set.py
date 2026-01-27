# Створення множини
numbers = {1, 2, 3, 3, 3, 4}

# Зверни увагу: трійки повторювались, але збереглась одна
print(numbers)
# Виведе: {1, 2, 3, 4}

# Перевірка наявності (дуже швидко)
print(2 in numbers)  # Виведе: True
print(54 in numbers)
print(1260 in numbers)

numbers.add(1260)
numbers.add(1261)
numbers.add(1269)

print(1260 in numbers)  # Виведе: True

# Додавання
numbers.add(5)
print(numbers)  # Виведе: {1, 2, 3, 4, 5}
