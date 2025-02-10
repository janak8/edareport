import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('cleaned_data.csv')

# Dashboard title
st.title("Data Dashboard")

# Display basic information
st.subheader("Basic Information")
st.write("Dataset Shape:", df.shape)
st.write("Column Names:", df.columns.tolist())
st.write("Data Types:")
st.write(df.dtypes)
st.write("Descriptive Statistics:")
st.write(df.describe())

# Handling missing values
st.subheader("Missing Values")
st.write("Missing Values Before Handling:")
st.write(df.isnull().sum())

# Fill missing 'Apply Date' with a placeholder
df['Apply Date'].fillna("Not Applied", inplace=True)

# Confirm missing values handled
st.write("Missing Values After Handling:")
st.write(df.isnull().sum())

# Visualize missing values
st.subheader("Missing Values Heatmap")
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
st.pyplot(plt)

# Clean categorical variables
df['Gender'] = df['Gender'].str.lower().str.strip()
df['Current Student Status'] = df['Current Student Status'].str.title()

# Visualize categorical distributions
st.subheader("Gender Distribution")
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Gender', palette='Set2')
st.pyplot(plt)

st.subheader("Current Student Status Distribution")
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Current Student Status', palette='Set3')
plt.xticks(rotation=45)
st.pyplot(plt)

# Scatter plot: Reward Amount vs. Skill Points Earned
st.subheader("Reward Amount vs. Skill Points Earned")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Reward Amount', y='Skill Points Earned', hue='Gender', palette='Set1')
st.pyplot(plt)

# Histogram: Reward Amount distribution
st.subheader("Reward Amount Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Reward Amount', bins=30, kde=True, color='blue')
st.pyplot(plt)

# Box plot: Reward Amount by Gender
st.subheader("Reward Amount by Gender")
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='Reward Amount', palette='Set2')
st.pyplot(plt)

# Gender distribution
st.subheader("Gender Distribution (Pie Chart)")
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen'])
st.pyplot(plt)

# Location analysis
st.subheader("Top 10 Countries by User Count")
location_counts = df['Country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=location_counts.index, y=location_counts.values, palette='Set3')
plt.xticks(rotation=45)
st.pyplot(plt)

# Correlation matrix for numeric columns
st.subheader("Correlation Matrix")
numeric_df = df.select_dtypes(include=['number'])

if numeric_df.shape[1] > 0:
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot(plt)
else:
    st.write("No numeric columns available for correlation analysis.")
