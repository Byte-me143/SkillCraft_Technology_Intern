
import pandas as pd
import matplotlib.pyplot as plt

xy = pd.read_csv("cenus.csv")


india = xy[xy['Country'] == 'India']


plt.figure(figsize=(8, 5))
plt.bar(india['Age_Group'], india['Population'],color='plum', edgecolor='black')

plt.title("India's Population Distribution by Age Group until 2022")
plt.xlabel("Age Group")
plt.ylabel("Population is in Millions")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


utx = xy.pivot(index='Age_Group', columns='Country', values='Population')

utx.plot(kind='bar', figsize=(10, 6), colormap='Set2', edgecolor='black')

plt.title("Population Distribution by Age Group until 2022")
plt.xlabel("Age Group")
plt.ylabel("Population is in Millions")
plt.xticks(rotation=0)
plt.legend(title="Country")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
