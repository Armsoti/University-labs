import csv
import os

flag = False
try:
    csvfile = open("lab9.csv","r")
    reader = csv.reader(csvfile, delimiter = ",")
    print("с1 : c2")
    for row in reader:
        print(row[0], ': ', row[1])
    csvfile.close()
except FileNotFoundError:
    print("Файл lab9.csv не знайдено!")
except IndexError:
    print("Помилка: у файлі є порожні рядки.")

min_value = float('inf')
max_value = float('-inf')
min_row = None
max_row = None

try:
    csvfile = open("lab9.csv","r")
    reader = csv.reader(csvfile, delimiter = ",")

    print("\nПошук min/max...")

    for row in reader:
        try:
            value_str = row[1]
            current_value = float(value_str.replace(',', '').replace('"', ''))
            if flag == False:
                flag = True

            if current_value > max_value:
                max_value = current_value
                max_row = row

            if current_value < min_value:
                min_value = current_value
                min_row = row

        except (ValueError, IndexError):
            pass

    csvfile.close()

    if flag == True:
        print(f"Знайдено! Максимум: {max_row[0]} ({max_row[1]})")
        print(f"Знайдено! Мінімум: {min_row[0]} ({min_row[1]})")

        with open("new_lab9.csv", "w", newline='') as csvfile2:
            writer = csv.writer(csvfile2, delimiter=";")
            writer.writerow(["Result", "Country (c1)", "Value (c2)"])
            writer.writerow(["Maximum", max_row[0], max_row[1]])
            writer.writerow(["Minimum", min_row[0], min_row[1]])

        print("Результати пошуку записано у файл new_lab9.csv")

    else:
        print("Не знайдено числових даних для пошуку min/max.")

except FileNotFoundError:
    print("Файл lab9.csv не знайдено!")