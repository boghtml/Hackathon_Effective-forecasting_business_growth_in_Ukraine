from flask import render_template, current_app as app
import pandas as pd
from .utils.analysis import analyze_data, analyze_dtypes, analyze_missing_values, analyze_unique_values
from .utils.visualization import visualize_data
from .utils.outliers import detect_outliers
from .utils.feature_importance import feature_importance

@app.route('/')
def index():
    data = pd.read_excel('app/static/uploads/dataset.xlsx')
    # Видалення рядків за умовою в колонці 'Дата'
    data.drop(data[data['Дата'] == 'Лопатка силікон з принтом 29,5*5*1см'].index, inplace=True)
    sample_data = data.head(5).to_html(classes='table table-striped', index=False)
    missing_values, data_description = analyze_data(data)
    unique_values = analyze_unique_values(data)
    dtypes = analyze_dtypes(data)
    missing_values_count = analyze_missing_values(data)

    missing_values, data_description = analyze_data(data)

    analysis = f"""
    Missing Values:<br>{missing_values.to_frame().to_html(classes='table table-striped')}<br><br>
    Data Description:<br>{data_description.to_html(classes='table table-striped')}<br><br>
    Unique Values:<br>{unique_values.to_frame().to_html(classes='table table-striped')}<br><br>
    Data Types:<br>{dtypes.to_frame().to_html(classes='table table-striped')}<br><br>
    Missing Values Count:<br>{missing_values_count.to_frame().to_html(classes='table table-striped')}
    """
    return render_template('reserv.html', sample_data=sample_data, analysis=analysis)

