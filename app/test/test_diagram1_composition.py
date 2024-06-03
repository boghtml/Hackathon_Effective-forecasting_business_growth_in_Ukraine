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

# Видалення рядків з некоректними значеннями в стовпці "Дата"
data = data[pd.to_datetime(data['Дата'], errors='coerce').notna()]

# Перетворення стовпця "Дата" на формат datetime
data['Дата'] = pd.to_datetime(data['Дата'])

# Перетворення стовпців "Кількість" та "Сума" на числові значення
data['Кількість'] = pd.to_numeric(data['Кількість'], errors='coerce')
data['Сума'] = pd.to_numeric(data['Сума'], errors='coerce')

# Групування даних за датами і підрахунок сум продажів
sales_by_date = data.groupby(data['Дата'].dt.date)['Сума'].sum()

# Створення кольорового градієнта
colors = plt.cm.viridis(np.linspace(0, 1, len(sales_by_date)))

# Створення діаграми
plt.figure(figsize=(10, 6))
plt.bar(sales_by_date.index, sales_by_date.values, color=colors)
plt.title('Сума продажів по датах')
plt.xlabel('Дата')
plt.ylabel('Сума продажів')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Збереження діаграми у файл
plt.savefig('diagram1_sum_period.png')

# Показ діаграми
plt.show()
