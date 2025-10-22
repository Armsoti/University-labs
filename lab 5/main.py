def showAll(StudentsMark):
    for i in StudentsMark:
        print(StudentsMark[i], "-", i)

def addStudent(StudentsMark, key, mark):
    StudentsMark[key] = mark
    print("Student", key, "add successfully")

def delStudent(StudentsMark, key):
    if key in StudentsMark:
        del StudentsMark[key]
        print("Student", key, "delete successfully")
    else:
        print("Student", key, "not exist")

def sortStudents(StudentsMark):
    sorted_dict = {k: StudentsMark[k] for k in sorted(StudentsMark)}
    print("Sorted dictionary")
    for i in sorted_dict:
        print(sorted_dict[i], "-", i)

def findMinAndMAx(StudentsMark):
    first_student_name = next(iter(StudentsMark))
    first_student_sum = sum(StudentsMark[first_student_name])
    student_max = first_student_name
    max_sum = first_student_sum
    student_min = first_student_name
    min_sum = first_student_sum

    for name, marks in StudentsMark.items():
        current_sum = sum(marks)
        print(name, ": сума =", current_sum)

        if current_sum > max_sum:
            max_sum = current_sum
            student_max = name

        if current_sum < min_sum:
            min_sum = current_sum
            student_min = name

    print("Student with max marks sum =", student_max, "with sum:", max_sum)
    print("Student with min marks sum =", student_min, "with sum:", min_sum)

StudentsMark = {
    "Кравченко Юлія Володимирівна": [3, 4, 5, 6, 7],
    "Оніщенко Максим Ігоревич": [2, 2, 2, 2, 2],
    "Барненко Ліза Вікторівна": [12, 12, 12, 10, 11],
    "Михайленко Ірина Анатоліївна": [12, 10, 8, 9, 2],
    "Ярмоленко Валентина Соломонівна": [10, 4, 5, 7, 8],
    "Барщук Аліса Марківна": [12, 12, 3, 4, 12],
    "Щербань Дарія Миколаївна": [10, 10, 9, 8, 7],
    "Ведмідь Юрій Ігоревич": [12, 5, 6, 8, 2],
}

showAll(StudentsMark)

a = input("Do you would like to add students? (y/n) ")
if a == "y":
    a = int(input("How many students do you want to add? "))
    while a < 1:
        a = int(input("Please enter a valid number:"))
    for i in range(a):
        key = input("Please enter students suename name and fathername:")
        mark = input("Please enter marks of student:")
        mark_list = [int(m.strip()) for m in mark.split(' ')]
        addStudent(StudentsMark, key, mark_list)

dell = input("Do you would like to delete students? (y/n) ")
if dell == "y":
    dell = int(input("How many students do you want to delete? "))
    while dell < 1:
        dell = int(input("Please enter a valid number:"))
    for i in range(dell):
        key = input("Please enter students suename name and fathername:")
        delStudent(StudentsMark, key)

sortStudents(StudentsMark)
findMinAndMAx(StudentsMark)