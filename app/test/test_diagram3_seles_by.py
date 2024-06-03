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

# Групування даних за підрозділами та категоріями, підрахунок загальної кількості продажів для кожної категорії в кожному підрозділі
sales_by_department_and_category = data.groupby(['Подразделение', 'ВидНоменклатури'])['Кількість'].sum().unstack()

# Створення кругових діаграм для кожного підрозділу
for department, sales in sales_by_department_and_category.iterrows():
    # Фільтрація категорій, які складають менше 2% від загальної кількості продажів
    total_sales = sales.sum()
    sales = sales[sales / total_sales * 100 >= 2.5]

    # Створення градієнтного кольорового масиву від фіолетового до зеленого
    num_categories = len(sales)
    gradient = np.linspace(0, 1, num_categories)
    colors = plt.cm.viridis(gradient)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sales.plot(kind='pie', ax=ax, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.set_title(department)
    ax.set_ylabel('')
    
    # Збереження діаграми у файл
    filename = f'diagram3_sales_by_{department.replace("/", "_").replace("\\", "_")}_pie.png'
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)  # Закриття фігури для звільнення пам'яті
