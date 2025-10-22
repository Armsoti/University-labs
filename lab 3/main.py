print("-" * 15 + "Завдання 1" + "-" * 15)
print("Присвойте змінній довільний рядок в та отримайте з неї наступні зрізи, якщо довжина слова достатня для виконання операції зрізу. Другу і передостанню літери слова")
task1_string = input("Введіть рядок(мін 2 символа): ")
length = len(task1_string)
while length < 2:
    task1_string = input("Помилка! Занадто короткий рядок! Введіть рядок(мін 2 символа): ")
    length = len(task1_string)

result = task1_string[0] + task1_string[2:-2] + task1_string[-1]
print(f"Вихідний рядок:", task1_string)
print("Нове слово", result)

print("-" * 15 + "Завдання 2" + "-" * 15)
print("Задане слово. Видалити з нього однакові символи, які розташовані поруч")
task2_string = input("Введіть рядок(мін 2 символа): ")
length2 = len(task2_string)
while length2 < 2:
    task2_string = input("Помилка! Занадто короткий рядок! Введіть рядок(мін 2 символа): ")
    length2 = len(task2_string)
new_word = task2_string[0]
i = 1

while i < length2:
    if task2_string[i] != task2_string[i-1]:
        new_word += task2_string[i]
    i += 1
print("Нове слово:", new_word)


print("-" * 15 + "Завдання 3" + "-" * 15)
print("Задано речення. Скласти програму, яка визначає і виводить на екран всі його слова, попередньо перетворивши кожне слово за таким правилом: замінити літеру «b» на «c».")
task3_string = str(input("Введіть рядок(мін 2 символа): "))
length3 = len(task3_string)
while length3 < 2:
    task3_string = input("Помилка! Занадто короткий рядок! Введіть рядок(мін 2 символа): ")
    length3 = len(task3_string)

print("Після заміни літери b на c: ", task3_string.replace("b", "c") )


