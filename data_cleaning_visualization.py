import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, None, 40],
    'Salary': [50000, 60000, None, 80000, 90000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data Cleaning
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Visualization
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary by Name')
plt.show()

# Statistical Analysis
print("Mean Age:", df['Age'].mean())
print("Median Salary:", df['Salary'].median())