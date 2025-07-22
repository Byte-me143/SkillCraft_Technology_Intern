import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

xy = pd.read_csv("ship.csv")

print(xy.info())
print(xy.describe())
print(xy.isnull().sum())

xy['Age'] = xy['Age'].fillna(xy['Age'].median())
xy['Embarked'] = xy['Embarked'].fillna(xy['Embarked'].mode()[0])
xy.drop(columns=['Cabin'], inplace=True)

xy['Sex'] = xy['Sex'].map({'male': 0, 'female': 1})
xy = pd.get_dummies(xy, columns=['Embarked'], drop_first=True)

sns.countplot(x='Survived', hue='Survived', palette='Set1', data=xy, legend=False)
plt.title("Survival Count")
plt.show()
print(xy['Survived'].value_counts(normalize=True))  

survival_rate = xy.groupby('Sex')['Survived'].mean().reset_index()
sns.barplot(x='Sex', y='Survived', hue='Sex', palette='Set3', data=survival_rate, legend=False)
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

sns.barplot(x='Pclass', y='Survived', hue='Pclass', data=xy, palette='Set2', errorbar=None, legend=False)
plt.title("Survival Rate by Passenger Class")
plt.show()

sns.histplot(xy['Age'], bins=30, kde=True, color='gold')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.histplot(data=xy, x='Age', hue='Survived', palette='pastel', legend=False, bins=30, kde=True)
plt.title("Survival by Age")
plt.show()


numeric_xy = xy.select_dtypes(include='number')
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_xy.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap of Numeric Features")
plt.show()


