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

# Перетворення стовпців "Кількість" та "Сума" на числові значення
data['Кількість'] = pd.to_numeric(data['Кількість'], errors='coerce')
data['Сума'] = pd.to_numeric(data['Сума'], errors='coerce')

# Групування даних за назвою товару і підрахунок сум продажів
sales_by_product = data.groupby('Номенклатура')['Сума'].sum()

# Сортування за сумою продажів
sales_by_product = sales_by_product.sort_values(ascending=False)

# Обмеження до 10 найпопулярніших товарів
top_n = 10
top_sales = sales_by_product.head(top_n)

plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(top_sales))) # Генеруємо градієнтний колір для кожного стовпця

bars = plt.barh(top_sales.index, top_sales.values, color=colors, alpha=0.7)
plt.title('Сума продажів 10 найпопулярніших товарів', fontsize=14)  # Вище за графіком, щоб підпис був збільшений
plt.xlabel('Сума продажів', fontsize=12)
plt.ylabel('Товар', fontsize=12)
plt.grid(True)
plt.gca().invert_yaxis()  # Інвертувати ось Y для найбільшого зверху

# Додавання підписів до стовпців
# Додавання підписів до стовпців
for bar, label in zip(bars, top_sales.values):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{label:.2f}', va='center', ha='left', fontsize=10, color='black')

plt.tight_layout()

# Збереження діаграми у файл
plt.savefig('diagram5_sales_by_product.png')

# Показ діаграми
plt.show()
