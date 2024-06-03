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

# Групування даних за підрозділами та підрахунок загальної кількості продажів для кожного підрозділу
sales_by_department = data.groupby('Подразделение')['Кількість'].sum()

# Створення градієнтного кольорового масиву від фіолетового до зеленого
num_colors = len(sales_by_department)
gradient = np.linspace(0, 1, num_colors)
colors = plt.cm.viridis(gradient)

# Створення кругової діаграми
plt.figure(figsize=(12, 7))
wedges, texts, autotexts = plt.pie(sales_by_department, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

# Центр та колір відсотків
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(8)

# Винесення підписів ліворуч з маленькими кольоровими квадратиками
plt.legend(wedges, [f'{dept} - {pct}' for dept, pct in zip(sales_by_department.index, [f'{p:.1f}%' for p in sales_by_department/sales_by_department.sum()*100])], title="Підрозділи", loc="center left", bbox_to_anchor=(-0.1, 0.5), fontsize='small', fancybox=True, shadow=True)

# Заголовок та рівні осі для кругової діаграми
plt.title('Кількість продажів по підрозділах')
plt.axis('equal')  

# Збереження діаграми у файл
plt.savefig('diagram4_sales_by_department_pie_with_legend.png', bbox_inches='tight')

# Показ діаграми
plt.show()
