import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('cleaned_data.csv')

# Basic information
print("Dataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nDescriptive Statistics:\n", df.describe())

# Handling missing values
print("\nMissing Values Summary Before Handling:\n", df.isnull().sum())

# Option 1: Drop rows with missing 'Apply Date'
# df = df.dropna(subset=['Apply Date'])

#Fill missing 'Apply Date' with a placeholder
df['Apply Date'].fillna("Not Applied", inplace=True)

# #Fill missing 'Apply Date' with the most common date
# most_common_date = df['Apply Date'].mode()[0]
# df['Apply Date'].fillna(most_common_date, inplace=True)

#Confirm missing values handled
print("\nMissing Values Summary After Handling:\n", df.isnull().sum())

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Clean categorical variables
df['Gender'] = df['Gender'].str.lower().str.strip()
df['Current Student Status'] = df['Current Student Status'].str.title()

#Visualize categorical distributions
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Gender', palette='Set2')
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Current Student Status', palette='Set3')
plt.title("Current Student Status Distribution")
plt.xticks(rotation=45)
plt.show()

# Scatter plot: Reward Amount vs. Skill Points Earned
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Reward Amount', y='Skill Points Earned', hue='Gender', palette='Set1')
plt.title("Reward Amount vs. Skill Points Earned")
plt.show()

# Histogram: Reward Amount distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Reward Amount', bins=30, kde=True, color='blue')
plt.title("Reward Amount Distribution")
plt.show()

# Box plot: Reward Amount by Gender
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='Reward Amount', palette='Set2')
plt.title("Reward Amount by Gender")
plt.show()




# Gender distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title("Gender Distribution")
plt.show()

# Location analysis
location_counts = df['Country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=location_counts.index, y=location_counts.values, palette='Set3')
plt.title("Top 10 Countries by User Count")
plt.xticks(rotation=45)
plt.show()

#Selecting only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Check if numeric_df is empty (no numeric columns)
if numeric_df.shape[1] > 0:
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()
else:
    print("No numeric columns available for correlation analysis.")

