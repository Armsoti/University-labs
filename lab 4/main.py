def find_dublicates(list2):
    dublicate_list = []
    print(list2)
    for i in range(len(list2)):
        k = list2[i]
        if k in dublicate_list:
            continue

        for j in range(i+1, len(list2)):
            if list2[j] == k:
                dublicate_list.append(k)
                break
    return dublicate_list

def add_elements_with_oddindex(list):
    second_list = []
    print(list)
    i = 0
    while i < len(list) :
        if i%2 == 0:
            print(list[i])
            second_list.append(list[i])
        i += 1
    return second_list

def is_prime(n):
    if n <= 1:
        return False
    # Перевіряємо дільники від 2 до квадратного кореня з n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def task5_list():
    z = []
    x = []
    y = []

    i = 8
    while i <= 22:
        z.append(i)
        i += 1
    print("Множина z", set(z))

    for i in range(len(z)):
        if z[i] > 0:
            x.append(z[i])

    print("Множина x", set(x))

    for i in range(len(z)):
        if is_prime(z[i]):
            y.append(z[i])

    print("Множина y", set(y))

print("-"*15, "Task 1", "-"*15)
print("Реалізувати одновимірний масив, довжину масива та сам масив користувач має ввести з клавіатури. Виконати над масивом обчислення, вказані  у Вашому варіанті")
print("Дано одномірний масив, що складається з N дійсних елементів. Масив користувач має ввести з клавіатури. Знайти максимальний від’ємний елемент.")

n = int(input("Введіть кількість елементів масиву:"))
while n < 0:
    n = int(input("Введіть кількість елементів більше 0"))
arr = []
print(f"Введіть {n} дійсних елементів (чисел):")
for i in range(n):
    element = float(input(f"Елемент {i + 1}: "))
    arr.append(element)

print("Початковий масив: ", arr)

negative_elements = [element for element in arr if element < 0]
if negative_elements:
    print(negative_elements)
    print ("Максимальний від’ємний елемент:", max(negative_elements))
else:
    print("Немає відємних елементів")


print("-"*15, "Task 2", "-"*15)
print("Заповнити двовимірний масив розміром 7x7 таким чином, як показано на рисунку згідно з Вашим варіантом. Вивести масив на екран. Для виконання завдання використовуйте цикли.")
N2 = 7
a = [[j-i for j in range(N2)] for i in range(N2)]
for row in a:
    print(*row)


print("-"*15, "Task 3", "-"*15)
print("Реалізувати функцію, яка виконує операції над списками – задану за варіантом та друк списку на екран. Список користувач має вводити з клавіатури.")
print("Доповнення списку у кінці елементами списку з парними індексами.")

list_input = input("Введіть елементи через побіл: ")
list = list_input.split(' ')
funtion_list = add_elements_with_oddindex(list)
final_list = list + funtion_list
print("Кінцевий список: ", final_list)


print("-"*15, "Task 4", "-"*15)
print("Реалізувати функцію, яка виконує операції над списками – задану за варіантом та друк списку на екран.")
print("Формування нового списку, у який входять елементи, що повторюються у попередньому списку.")

list2_input = input("Введіть елементи через побіл: ")
list2 = list2_input.split(' ')
repeat_items = find_dublicates(list2)
print("Введений список:", list2)
print("Список повторюваних елементів:", repeat_items)


print("-"*15, "Task 5", "-"*15)
print("Реалізувати функцію, яка виконує операції над множинами – задану за варіантом та друк множини на екран. У випадку, якщо задану варіантом операцію над множиною виконати не можна, перетворіть множину у список, а потім при виведенні на екран результуючий список перетворіть на множину.")
print("Маємо три множини x, y, z цифр {8,9,10,11, …, 21,22}. Змінній х присвоїти множину всіх цілих чисел від 8 до 22, змінній у – множину всіх простих чисел з цього діапазону")
list_5 = task5_list()

