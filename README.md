# Data Cleaning & Preprocessing – Titanic Dataset

This project performs data cleaning and preprocessing using Python for the Elevate Labs AI & ML Internship.

## Steps Performed:

1. **Explored Data**
   - Used `info()`, `isnull().sum()`, and `describe()`

2. **Handled Missing Values**
   - Filled 'Age' with median
   - Filled 'Embarked' with mode

3. **Encoded Categorical Features**
   - LabelEncoded 'Sex'
   - One-hot encoded 'Embarked'

4. **Scaled Numerical Features**
   - Used MinMaxScaler on 'Age' and 'Fare'

5. **Visualized and Removed Outliers**
   - Used boxplots and removed extreme values from 'Fare'

6. **Saved Output Files**
   - `titanic.csv`
   - `boxplots.png`

## Libraries Used
- pandas
- numpy
- seaborn
- matplotlib
- sklearn
