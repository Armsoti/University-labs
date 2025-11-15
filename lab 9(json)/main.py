import json
import os

DATA_FILE = 'students_grades.json'
RESULT_FILE = 'grade_analysis.json'


def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        print(f"Створюю початковий файл {DATA_FILE}...")
        initial_students = [
            {"surname": "Петренко", "grades": [8, 9, 10, 7, 8]},
            {"surname": "Іваненко", "grades": [10, 11, 10, 12, 9]},
            {"surname": "Сидоренко", "grades": [5, 6, 5, 7, 6]},
            {"surname": "Ковальчук", "grades": [12, 12, 11, 10, 12]},
            {"surname": "Мельник", "grades": [7, 8, 9, 8, 7]},
            {"surname": "Шевченко", "grades": [9, 9, 9, 9, 9]},
            {"surname": "Бондаренко", "grades": [10, 8, 11, 9, 10]},
            {"surname": "Ткаченко", "grades": [6, 7, 8, 7, 6]},
            {"surname": "Павленко", "grades": [11, 10, 9, 11, 10]},
            {"surname": "Захарченко", "grades": [8, 7, 9, 10, 8]}
        ]
        save_data(initial_students)


def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Помилка: Файл {DATA_FILE} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка: Файл {DATA_FILE} має невірний формат JSON.")
        return []


def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Помилка при записі у файл {DATA_FILE}: {e}")


def view_students():
    print(f"\n--- Вміст файлу {DATA_FILE} ---")
    students = load_data()
    if not students:
        print("Список учнів порожній.")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. Прізвище: {student['surname']}, Оцінки: {student['grades']}")
    print("-" * (26 + len(DATA_FILE)))


def add_student():
    print("\n--- Додавання нового учня ---")
    students = load_data()

    surname = input("Введіть прізвище учня: ").strip()
    if not surname:
        print("Помилка: Прізвище не може бути порожнім.")
        return

    grades = []
    for i in range(5):
        while True:
            try:
                grade = int(input(f"Введіть оцінку з предмету {i + 1}: "))
                if 0 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Помилка: Оцінка має бути від 0 до 12.")
            except ValueError:
                print("Помилка: Введіть число.")

    new_student = {"surname": surname, "grades": grades}
    students.append(new_student)
    save_data(students)
    print(f"Учня {surname} успішно додано.")


def delete_student():
    print("\n--- Видалення учня ---")
    students = load_data()
    if not students:
        print("Список учнів порожній. Нема чого видаляти.")
        return

    surname_to_delete = input("Введіть прізвище учня для видалення: ").strip()

    students_to_keep = []
    found = False
    for student in students:
        if student['surname'].lower() == surname_to_delete.lower():
            found = True
            print(f"Учня {student['surname']} з оцінками {student['grades']} видалено.")
        else:
            students_to_keep.append(student)

    if not found:
        print(f"Помилка: Учня з прізвищем '{surname_to_delete}' не знайдено.")
    else:
        save_data(students_to_keep)


def search_student():
    print("\n--- Пошук учня за прізвищем ---")
    students = load_data()
    if not students:
        print("Список учнів порожній.")
        return

    surname_to_find = input("Введіть прізвище для пошуку: ").strip().lower()

    results = []
    for student in students:
        if surname_to_find in student['surname'].lower():
            results.append(student)

    if not results:
        print(f"Учнів з прізвищем, що містить '{surname_to_find}', не знайдено.")
    else:
        print(f"Знайдено {len(results)} учнів:")
        for student in results:
            print(f" - Прізвище: {student['surname']}, Оцінки: {student['grades']}")


def analyze_grades():
    print("\n--- Аналіз успішності ---")
    students = load_data()
    if not students:
        print("Недостатньо даних для аналізу.")
        return

    student_max_sum = None
    student_min_sum = None
    max_sum = -1
    min_sum = float('inf')

    for student in students:
        current_sum = sum(student['grades'])

        if current_sum > max_sum:
            max_sum = current_sum
            student_max_sum = student['surname']

        if current_sum < min_sum:
            min_sum = current_sum
            student_min_sum = student['surname']

    result_data = {
        "student_with_max_sum": {
            "surname": student_max_sum,
            "sum_of_grades": max_sum
        },
        "student_with_min_sum": {
            "surname": student_min_sum,
            "sum_of_grades": min_sum
        }
    }

    try:
        with open(RESULT_FILE, 'w', encoding='utf-8') as file:
            json.dump(result_data, file, indent=4, ensure_ascii=False)
        print(f"Аналіз завершено. Результати записано у файл {RESULT_FILE}.")
        print(f"Учень з найбільшою сумою балів ({max_sum}): {student_max_sum}")
        print(f"Учень з найменшою сумою балів ({min_sum}): {student_min_sum}")
    except IOError as e:
        print(f"Помилка при записі у файл {RESULT_FILE}: {e}")


def main_menu():
    initialize_data_file()

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Вивести список учнів")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Пошук учня за прізвищем")
        print("5. Аналіз успішності (Завдання за варіантом)")
        print("6. Вихід")

        choice = input("Оберіть опцію (1-6): ").strip()

        if choice == '1':
            view_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            analyze_grades()
        elif choice == '6':
            print("Дякую за роботу. До побачення!")
            break
        else:
            print("Помилка: Невірний вибір. Будь ласка, введіть число від 1 до 6.")


if __name__ == "__main__":
    main_menu()