import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xy = pd.read_csv("accident.csv")  

print(xy.head())

print("Columns:", xy.columns)

plt.figure(figsize=(10, 6))
sns.countplot(x='Road_Pos', data=xy, hue='Road_Pos', palette='Set3', legend=False)
plt.title("Accidents by Road Condition", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Wea_Pos', data=xy, hue='Wea_Pos', palette='Set2', legend=False)
plt.title("Accidents by Weather")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

if 'Time' in xy.columns:
    xy['Time'] = pd.to_datetime(xy['Time'], format='%H:%M:%S', errors='coerce')
    xy['Hour'] = xy['Time'].dt.hour
    plt.figure(figsize=(8, 5))
    sns.histplot(xy['Hour'], bins=24, kde=False)
    plt.title("Accidents by Hour")
    plt.xlabel("Hour of Day (0-23)")
    plt.tight_layout()
    plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Latitude', data=xy, hue='Latitude', palette='Set1', legend=False)
plt.title("Latitude")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Longitude', data=xy, hue='Longitude', palette='pastel', legend=False)
plt.title("Latitude")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

if 'Date' in xy.columns:
    xy['Date'] = pd.to_datetime(xy['Date'], format='%d-%m-%Y', errors='coerce')
    xy['Year'] = xy['Date'].dt.year
    plt.figure(figsize=(8, 5))
    sns.histplot(xy['Year'], bins=15, kde=False)
    plt.title("Accidents by Year")
    plt.xlabel("Year")
    plt.tight_layout()
    plt.show()

