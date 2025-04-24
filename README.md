# Data Cleaning & Preprocessing - Titanic Dataset

This project performs data cleaning and preprocessing on the Titanic dataset as part of the Elevate Labs AI & ML Internship. [cite: 1, 4]

## Task Objective

The objective of this task is to learn how to clean and prepare raw data for Machine Learning (ML) models. [cite: 1]

## Tools Used

- Python [cite: 2]
- Pandas [cite: 2]
- NumPy [cite: 2]
- Matplotlib/Seaborn [cite: 2]
- Scikit-learn

## Steps Performed

1.  **Explored Data:**
    -Loaded the dataset using Pandas.
    - Inspected the data using `head()`, `info()`, `isnull().sum()`, and `describe()`. [cite: 2]
2.  **Handled Missing Values:** [cite: 3]
    - Filled missing 'Age' values with the median.
    - Filled missing 'Embarked' values with the mode.
3.  **Converted Categorical Features:** [cite: 3]
    - Converted the 'Sex' column to numerical using Label Encoding.
    - Converted the 'Embarked' column to numerical using One-Hot Encoding.
4.  **Normalized Numerical Features:** [cite: 4]
    - Scaled the 'Age' and 'Fare' columns using MinMaxScaler.
5.  **Visualized and Removed Outliers:** [cite: 4]
    - Used boxplots to visualize outliers in the 'Age' and 'Fare' columns. [cite: 4]
    - Removed outliers from the 'Fare' column.

## Files Included

* `data_preprocessing.py`: Python script containing the data cleaning and preprocessing code.
* `titanic.csv`: The Titanic dataset used in this project.
* `age_boxplot.png`: (Optional) Boxplot visualization of Age outliers.
* `fare_boxplot.png`: (Optional) Boxplot visualization of Fare outliers.
* `README.md`: This file, providing an overview of the project. [cite: 15]

## How to Run the Code

1.  Ensure you have Python and the required libraries installed (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn).
2.  Place the `titanic.csv` file in the same directory as `data_preprocessing.py`.
3.  Run the `data_preprocessing.py` script.

## Self-Learning and Debugging

As per the task guidelines, I have independently researched and debugged to complete this task. [cite: 11, 12]

## Contact

 Jaieep Kushwah
