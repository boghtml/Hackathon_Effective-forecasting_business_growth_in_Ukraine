from scipy.stats import zscore

def detect_outliers(data):
    # Обчислення Z-score для кожної числової колонки
    z_scores = data.select_dtypes(include=['float64', 'int64']).apply(zscore)
    # Виявлення викидів (значення Z-score > 3 або < -3)
    outliers = z_scores[(z_scores > 3) | (z_scores < -3)].dropna(how='all')
    return outliers
