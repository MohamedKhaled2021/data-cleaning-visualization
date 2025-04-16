# Ensure required libraries are installed
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.stats import ttest_ind
except ImportError as e:
    print("Missing library:", e.name)
    print("Please install it using: pip install", e.name)
    exit(1)

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

# Advanced Data Cleaning: Handle outliers
q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# Visualization
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary by Name')
plt.show()

# Additional Visualizations
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Age vs Salary')
plt.show()

# Statistical Analysis
print("Mean Age:", df['Age'].mean())
print("Median Salary:", df['Salary'].median())

# Correlation Analysis
correlation = df.corr()
print("Correlation Matrix:\n", correlation)

# Hypothesis Testing
group1 = df[df['Age'] < 30]['Salary']
group2 = df[df['Age'] >= 30]['Salary']
t_stat, p_value = ttest_ind(group1, group2)
print("T-test Results: t_stat=", t_stat, ", p_value=", p_value)