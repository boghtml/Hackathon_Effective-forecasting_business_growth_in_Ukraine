import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

def feature_importance(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    if y.dtype == 'object':
        le = LabelEncoder()
        y = le.fit_transform(y)


    numerical_features = X.select_dtypes(include=['number']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    label_encoders = {column: LabelEncoder() for column in categorical_features}
    for column in categorical_features:
        X[column] = label_encoders[column].fit_transform(X[column])


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    importances = model.feature_importances_
    feature_importance = pd.Series(importances, index=X.columns).sort_values(ascending=False)

    return feature_importance