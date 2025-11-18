import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Task 1
# Побудуйте графік функції. Оберіть суцільний тип лінії, задайте колір та товщину графіку та позначте осі,
# виведіть назву графіка на екран, вставте легенду. Використайте бібліотеку Matplotlib.
def f(x):
    y= np.cos(x ** 2)
    return y

x_values = np.arange(0, 10, 0.1)
y_values = f(x_values)

plt.plot(x_values, y_values, linestyle='solid', color='red', linewidth=2, label='y=cos(x^2)')
plt.title("Графік функції y=cos(x^2)")         # Назва графіка
plt.xlabel("Вісь X")  # Підпис горизонтальної осі
plt.ylabel("Вісь Y")
plt.legend()
plt.show()

#Task 2.1
#На одній координатній осі побудуйте графіки, що показують динаміку показника для двох країн,
#підпишіть осі –  по осі Х має відображатися рік, а по осі Y має відображатися значення показника.#

try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("Помилка: файл 'data.csv' не знайдено.")
    exit()

x = data['Year']
y = data['Albania']
z = data['Ukraine']

plt.plot(x, z, label='Ukraine', color = "purple")
plt.plot(x, y, label='Albania', color = "yellow")

plt.title('Population, ages 7-11, total', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Indicator', fontsize=12, color='red')

plt.legend()
plt.grid(True)
plt.show()

#Task 2.2
#Побудуйте стовпчасті діаграми, які відображатимуть значення показника для кожної з країн.
# Назву країни для побудови діаграми має вводити користувач з клавіатури.

try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("Помилка: файл 'data.csv' не знайдено.")
    exit()

available_countries = [col for col in data.columns if col != 'Year']
print(f"Доступні країни: {', '.join(available_countries)}")
country_name = input("Введіть назву країни для діаграми: ")
country_name = country_name.strip().title()

if country_name not in available_countries:
    print(f"Помилка: Країну '{country_name}' не знайдено.")
    print(f"Доступні варіанти: {available_countries}")
    exit()

x = data['Year']
y = data[country_name]

plt.bar(x, y, color = "purple")

plt.title(f'Population, ages 7-11, total in {country_name}', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Indicator', fontsize=12, color='red')

plt.grid(True)
plt.show()

#Task 3
#Побудуйте кругову діаграму на основі даних з предметної області лабораторної роботи №9 (дані з JSON).
#Використайте бібліотеку Matplotlib. На круговій діаграмі мають відображатися значення показників у відсотках, наприклад,
#відсоток дівчат та хлопців, які навчаються у певному класі, сектори діаграми повинні бути розфарбовані в різний колір,
#на діаграмі мають бути підписи.


try:
    df = pd.read_json('students_grades.json')
except FileNotFoundError:
    print("Помилка: файл 'students_grades.json' не знайдено.")
    exit()
except Exception as e:
    print(f"Помилка читання JSON: {e}")
    exit()

all_grades = df['grades'].explode()
grade_counts = all_grades.value_counts()
labels = grade_counts.index.astype(str)
sizes = grade_counts.values

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(sizes,
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  textprops=dict(color="w"))

legend_labels = [f"Оцінка: {label}" for label in labels]

ax.legend(wedges, legend_labels,
          title="Оцінки",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=10, weight="bold")
ax.set_title("Розподіл усіх оцінок студентів (%)")
ax.axis('equal')

plt.show()