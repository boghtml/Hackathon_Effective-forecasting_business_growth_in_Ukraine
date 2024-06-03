import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def visualize_data(data):
    # Визуалізація розподілу даних
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_data.empty:
        numeric_data.hist(bins=50, figsize=(20, 15))
        plt.savefig('hackaton/hackaton2/app/static/images/histogram.png')
        plt.close()
    else:
        print("No numerical columns found for histogram visualization.")

    # Boxplot для кожної числової колонки
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_data.empty:
        numeric_data.plot(kind='box', subplots=True, layout=(2, 3), figsize=(15, 10), title='Boxplot for Numerical Columns')
        plt.savefig('hackaton/hackaton2/app/static/images/boxplot.png')
        plt.close()
    else:
        print("No numerical columns found for boxplot visualization.")

    # Видалення нечислових даних для кореляційної матриці
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_data.empty:
        # Кореляційна матриця
        plt.figure(figsize=(15, 10))
        sns.heatmap(numeric_data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.savefig('hackaton/hackaton2/app/static/images/correlation_matrix.png')
        plt.close()
    else:
        print("No numerical columns found for correlation matrix visualization.")

    # Розподіл кожної змінної
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_data.empty:
        for column in numeric_data.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(data[column].dropna(), kde=True)
            plt.title(f'Distribution of {column}')
            plt.savefig(f'hackaton/hackaton2/app/static/images/distribution_{column}.png')
            plt.close()
    else:
        print("No numerical columns found for distribution visualization.")