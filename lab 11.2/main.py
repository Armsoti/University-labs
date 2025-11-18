import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('data.csv',

                       sep=',', encoding='latin1',

                       parse_dates=['Date'], dayfirst=True,

                       index_col='Date')

df = pd.read_csv('data.csv',
                 parse_dates=['Date'],
                 index_col='Date')

print("Start")
print(df.head())
print(df.info())
print(df.describe())
lane_columns = ['Rachel / Papineau', 'Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf', 'Parc', 'PierDup', 'CSC (Côte Sainte-Catherine)', 'Pont_Jacques_Cartier', 'Totem_Laurier', 'Notre-Dame', 'Rachel / Hôtel de Ville', 'Saint-Antoine', 'René-Lévesque', 'Viger', 'Boyer', 'Maisonneuve_3', 'University']

total_cyclists = df[lane_columns].sum().sum()
print(f"\nЗагальна кількість{total_cyclists}")

total_per_lane = df[lane_columns].sum()
print("\nЗагальна кількість (кожна доріжка):")
print(total_per_lane)


if 'Date' in df.columns:
    df = df.set_index('Date')
elif df.index.dtype != 'datetime64[ns]':
    print("Помилка: Не вдалося знайти стовпець дати для індексації.")
    exit()

monthly_totals = df[lane_columns].resample('ME').sum()

print("\nНайпопулярніший місяць (для кожної доріжки):")
for lane in lane_columns:
    try:
        popular_month = monthly_totals[lane].idxmax()
        print(f"  {lane}: {popular_month.strftime('%B %Y')}")
    except Exception as e:
        print(f" Помилка при обробці {lane}: {e}")

lane_to_plot = lane_columns[0]

print(f"\nграфік для {lane_to_plot}")

try:
    monthly_totals[lane_to_plot].plot(kind='bar', figsize=(10, 6))

    plt.title(f"Місячна завантаженість: {lane_to_plot}")
    plt.ylabel("Кількість велосипедистів")
    plt.xlabel("Місяць")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Не вдалося побудувати графік: {e}")