# Hackathon_Effective-forecasting_business_growth_in_Ukraine
## Main Task

The primary objective of this hackathon project was to augment the dataset with external factors influential for demand forecasting and to determine which factors (both provided and external) are most significant for demand prediction.

## Functional Requirements

- Loading External Factors: The dataset is supplemented with factors affecting demand forecasting.
- Determining Factor Influence: Users can see how specific factors affect demand (whether demand increases or decreases).

## Our Solution
- Data Augmentation: We added seasonal factors such as month, day of the week, and time of day to the existing dataset to capture their influence on sales patterns.
- Machine Learning Models: We utilized multiple machine learning algorithms including RandomForest, GradientBoosting, and LinearRegression to forecast sales and compared their accuracy to determine the best performing model.

By incorporating these additional seasonal factors, we were able to improve the accuracy of our sales forecasts, providing valuable insights and reliable predictions to aid in business growth strategies.

## Project Description

This project is designed for analyzing and forecasting sales based on historical data. It includes data analysis, visualization, and the use of machine learning methods to predict sales considering external factors such as seasonality.

### Detailed Description of Folders and Files:

- **app/**: The main project folder.
  - **static/**: Contains static files such as CSS, images, and uploads.
    - **css/**: Styles for the web interface.
    - **images/**: Images used in the project.
    - **jquery/**: Scripts for dynamic interaction with page elements.
    - **uploads/**: Input data files.
  - **templates/**: HTML templates for the web interface.
  - **test/**: Scripts for testing and an additional dataset for tests.
  - **utils/**: Utilities for data analysis, determining feature importance, detecting outliers, and visualization.
    - **analysis.py**: Scripts for data analytics.
    - **feature_importance.py**: Determining feature importance.
    - **outliers.py**: Detecting outliers in the data.
    - **visualization.py**: Data visualization.
  - **routes.py**: Routes for the web application.
  - **config.py**: Configuration settings for the application.
  - **run.py**: Main file for running the application.

### Technologies Used
#### Backend
- **Python**: The core programming language used for data analysis and machine learning.
- **Flask**: A lightweight WSGI web application framework used for the web server and routing.
- **Pandas**: A data manipulation and analysis library.
- **Scikit-learn**: A machine learning library for Python, used for implementing and evaluating various models.
#### Frontend
- **HTML/CSS**: For structuring and styling the web interface.
- **JavaScript**: For dynamic interaction with the web interface.
- **JQuery**: A fast, small, and feature-rich JavaScript library.

## Features

- **Data Analysis**: Includes checking data for missing values, determining statistical characteristics, and detecting outliers.
- **Data Visualization**: Building charts for better understanding of the data, including the impact of seasonal factors on sales.
- **Machine Learning**: Using RandomForest, GradientBoosting, and LinearRegression algorithms for sales forecasting. Comparing models by accuracy.

## Advantages

- **Comprehensive Analysis**: The project provides a thorough analysis of sales data, identifying patterns and trends.
- **Visual Insights**: The visualizations help in understanding the data better, making it easier to communicate findings.
- **Accurate Forecasting**: By using multiple machine learning models, the project ensures accurate sales forecasting, taking into account various external factors.
- **Extendable and Customizable**: The modular structure allows for easy extension and customization of the project to include additional features or different datasets.

## Results / Functionality

![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/b1a35c9f-668f-49a3-8f9d-6668d50bd54c)
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/0530713f-3ecd-4a01-beec-a92d0775b95a)
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/4ee3eb10-fcaa-4fda-b634-558ae035b537)
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/1d530fbc-a57d-4b9c-8e76-ffebebfc02c1)

### Results of machine learning
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/9d74aea8-d30b-4d54-a741-73e449d7bd65)
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/65c96f73-0f3b-4c6b-89a8-e301a35b9dd5)

### Results after adding seasonality
![image](https://github.com/boghtml/Hackathon_Effective-forecasting_business_growth_in_Ukraine/assets/119760440/144c2ab7-72b6-4feb-9802-a21ffcf3f840)

## Usage

1. Clone the repository.
2. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt

## Summary

The project leverages historical sales data and enhances it with seasonal factors to improve the accuracy of sales predictions. The detailed data analysis and visualization components offer deep insights into sales patterns, while the machine learning models provide robust forecasting capabilities. The project's structure and code are designed for easy extension, allowing for the addition of new features and datasets as needed.
