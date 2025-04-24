import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load dataset
df = pd.read_csv("titanic.csv")

# 1. Explore
print("\nFirst 5 Rows:\n", df.head())
print("\nInfo:\n", df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Stats:\n", df.describe())

# 2. Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
print("\nMissing values after handling:\n", df.isnull().sum())

# 3. Encode categorical features
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])  # Male = 1, Female = 0
df = pd.get_dummies(df, columns=['Embarked'])

# 4. Scale numerical features
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print("\nData after scaling:\n", df.describe())

# 5. Visualize outliers
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title("Boxplot of Age")
plt.subplot(1, 2, 2)
sns.boxplot(y=df['Fare'])
plt.title("Boxplot of Fare")
plt.tight_layout()
plt.savefig("boxplots.png")
plt.show()

# 6. Handle outliers in 'Fare'
df = df[df['Fare'] < (df['Fare'].mean() + 3 * df['Fare'].std())]
print("\nData after handling outliers:\n", df.describe())

# 7. Save the cleaned data
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'titanic_cleaned.csv'")
