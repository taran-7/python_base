# --- 1. ЗАПИС У ФАЙЛ (mode='w') ---
# 'w' (write) - створює файл (або ПЕРЕЗАПИСУЄ існуючий).
# Увага: старий вміст файлу буде знищено!


import os
# print("--- 1. Створюємо файл my_notes.txt ---")

# with open('my_notes.txt', 'w', encoding='utf-8') as file:
#     file.write("Це перший рядок у файлі.\n")  # \n переносить на новий рядок
#     file.write("Python - це круто!\n")

# print("Файл успішно створено!")

# # --- 2. ЧИТАННЯ З ФАЙЛУ (mode='r') ---
# # 'r' (read) - відкриває тільки для читання. Це режим за замовчуванням.

# print("\n--- 2. Читаємо файл ---")

# with open('my_notes.txt', 'r', encoding='utf-8') as file:
#     content = file.read()  # Читає ВЕСЬ файл у змінну
#     print(f"Вміст файлу:\n{content}")


# # --- 3. ДОДАВАННЯ У ФАЙЛ (mode='a') ---
# # 'a' (append) - додає дані в КІНЕЦЬ файлу, не стираючи старе.

# print("--- 3. Дописуємо новий рядок ---")

# with open('my_notes.txt', 'a', encoding='utf-8') as file:
#     file.write("Цей рядок було додано пізніше.\n")

# # Перевіримо результат, прочитавши файл ще раз, але порядково
# print("\n--- Перевірка (читаємо порядково) ---")
# with open('my_notes.txt', 'r', encoding='utf-8') as file:
#     for line in file:  # Файл можна перебирати циклом як список!
#         print(f"Рядок: {line.strip()}")  # .strip() прибирає зайві переноси рядків


# --- 4. ПРАКТИЧНЕ ЗАВДАННЯ ---
# Розкоментуй код нижче та допиши його.
# Твоє завдання:
# 1. Створити список гостей: guests = ["Олег", "Марія", "Андрій"]
my_guests = ["Олег", "Марія", "Андрій"]

# 2. Записати кожного гостя у файл 'guest_list.txt' з нового рядка.
with open("guest_list.txt", "w", encoding="utf-8") as f:
    for guest in my_guests:
        f.write(guest + "\n")
# guests = ["Олег", "Марія", "Андрій"]
# with open('guest_list.txt', 'w', encoding='utf-8') as f:
#     # Твій цикл тут:
#     pass
print("\nСписок гостей записано!")
# print("\nСписок гостей записано!")

with open('guest_list.txt', 'r', encoding='utf-8') as file:
    print("Список гостей:")
    for line in file:
        print(line.strip())


os.remove("guest_list.txt")
