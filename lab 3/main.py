# Присвойте змінній довільний рядок в та отримайте з неї наступні зрізи, якщо довжина слова достатня для виконання операції зрізу.
# Другу і передостанню літери слова

print("-" * 15 + "Завдання 1" + "-" * 15)
print("Присвойте змінній довільний рядок в та отримайте з неї наступні зрізи, якщо довжина слова достатня для виконання операції зрізу.hДругу і передостанню літери слова")
task1_string = input("Введіть рядок(мін 2 символа): ")
length = len(task1_string)
while length < 2:
    b_string = input("Помилка! Занадто короткий рядок! Введіть рядок(мін 2 символа): ")
    length = len(b_string)

second_char = task1_string[1]
second_to_last_char = task1_string[-2]
result = second_char + second_to_last_char

print(f"Вихідний рядок:", task1_string)
print(f"Друга літера:",second_char)
print(f"Передостання літера:", second_to_last_char)
print(f"Результат (зріз):", result)

print("-" * 15 + "Завдання 2" + "-" * 15)
print("Задане слово. Видалити з нього однакові символи, які розташовані поруч")
task2_string = input("Введіть рядок(мін 2 символа): ")
length2 = len(task2_string)
while length2 < 2:
    b_string = input("Помилка! Занадто короткий рядок! Введіть рядок(мін 2 символа): ")
    length2 = len(b_string)
new_word = task2_string[0]
for i in range(1, len(task2_string)):
    if task2_string[i] != task2_string[i - 1]:
        new_word += task2_string[i]
print(f"Результат: {new_word}")

print("-" * 15 + "Завдання 3" + "-" * 15)



