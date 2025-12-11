# Melbourne House Price Prediction

Predict house prices in Melbourne using machine learning techniques. This project includes data preprocessing, exploratory data analysis (EDA), model building using XGBoost, evaluation, and an interactive Streamlit app for prediction.

---

## Table of Contents
- [About](#about)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributing](#contributing)

---

## About
Housing price prediction is a common regression problem in data science.  
This project predicts Melbourne house prices based on historical data, considering factors such as location, number of rooms, house type, and distance from the city center.

---

## Dataset
The dataset is sourced from [Kaggle: Melbourne Housing Data](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot).  
It includes the following key features:
- `Suburb` – location of the house
- `Rooms` – number of rooms
- `Type` – house type (h, t, u)
- `Price` – target variable (house price)
- `Distance` – distance from city center
- Additional features such as `Bathroom`, `Car`, `Landsize`, `BuildingArea`, `YearBuilt`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/melbourne-house-price-prediction.git
   cd melbourne-house-price-prediction


   Usage

Launch the Streamlit app.

Input house details such as suburb, rooms, type, etc.

Click Predict to see the estimated house price.

Explore data visualizations and insights in the app.

Features

Data Cleaning and Preprocessing

Handling Missing Values

Feature Engineering

Exploratory Data Analysis (EDA)

Data Visualization with Matplotlib and Seaborn

XGBoost Regression Model

Model Evaluation using MAE and R²

Interactive Streamlit App for prediction

Model

Algorithm: XGBoost Regressor

Evaluation Metrics: Mean Absolute Error (MAE), R² Score

Preprocessing: Handling missing values, encoding categorical variables, feature scaling

License

This project is licensed under the MIT License.

Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit pull requests.


   pip install -r requirements.txt

   streamlit run app.py
