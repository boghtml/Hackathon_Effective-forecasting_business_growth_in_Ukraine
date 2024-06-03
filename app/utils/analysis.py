import pandas as pd

def analyze_data(data):
    # Перевірка на пропущені значення
    missing_values = data.isnull().sum()
    # Статистичний опис даних
    data_description = data.describe(include='all')
    return missing_values, data_description

def analyze_unique_values(data):
    # Аналіз унікальних значень
    unique_values = data.nunique()
    return unique_values

def analyze_dtypes(data):
    # Аналіз типів даних
    dtypes = data.dtypes
    return dtypes

def analyze_missing_values(data):
    # Аналіз кількості пропущених значень
    missing_values_count = data.isnull().sum()
    return missing_values_count
