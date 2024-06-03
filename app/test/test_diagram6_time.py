import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Вказання повного шляху до файлу
filename = 'Data_set.xlsx'
filepath = os.path.join('C:\\', 'Users', 'Computer', 'hackaton', 'test', filename)

# Спроба завантажити файл
try:
    data = pd.read_excel(filepath)
except FileNotFoundError:
    print(f"Файл не знайдено за шляхом: {filepath}")
    exit()

# Перетворення стовпців "Дата" на тип datetime, з вказанням формату дати
data['Дата'] = pd.to_datetime(data['Дата'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Видалення рядків з невалідними датами
data = data.dropna(subset=['Дата'])

# Виділення години з дати
data['Hour'] = data['Дата'].dt.hour

# Створення повного ряду для всіх годин дня
full_hour_range = pd.date_range(start=data['Дата'].min().floor('D'), end=data['Дата'].max().ceil('D'), freq='H')

# Об'єднання даних з повним рядом годин і вибірку з покупками
hourly_data = pd.DataFrame(index=full_hour_range)
hourly_data['Кількість'] = data.groupby(data['Дата'].dt.floor('H')).size()
hourly_data['Кількість'] = hourly_data['Кількість'].fillna(0)  # Заповнення пропущених значень нулями

# Фільтрація даних для виключення ночі (з 6:00 до 22:00)
daytime_data = hourly_data.between_time('06:00', '22:00')

# Створення інтервалів для групування даних (наприклад, кожні 2 години)
time_bins = range(6, 22, 2)

# Групування даних за інтервалами годин та підрахунок кількості відвідувань
visits_by_hour = daytime_data.groupby(daytime_data.index.hour // 2 * 2).sum()

# Створення графіку з градієнтним кольором від фіолетового до зеленого
colors = plt.cm.viridis(np.linspace(0, 1, len(visits_by_hour)))
plt.figure(figsize=(10, 6))
bars = plt.bar(visits_by_hour.index, visits_by_hour['Кількість'], color=colors)

plt.title('Кількість відвідувань за часом дня', fontsize=14)
plt.xlabel('Година', fontsize=12)
plt.ylabel('Кількість відвідувань', fontsize=12)

plt.xticks(visits_by_hour.index, [f"{hour}:00-{hour+2}:00" for hour in visits_by_hour.index], rotation=45)
plt.tight_layout()

# Збереження діаграми у файл
plt.savefig('diagram6_visits_by_hour_gradient.png')

# Показ діаграми
plt.show()
