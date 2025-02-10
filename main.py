import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="EDA Report Dashboard", layout="wide")

# Title and introduction
st.title("Exploratory Data Analysis (EDA) Report")
st.markdown("""
### Introduction
Welcome to the EDA Report Dashboard! This interactive app provides a detailed exploratory data analysis
of the dataset. We will clean the data, handle missing values, and visualize patterns to gain meaningful insights.

#### What We Are Analyzing:
- Understanding dataset structure
- Handling missing values
- Cleaning categorical variables
- Visualizing distributions and relationships
""")

# Load dataset
st.header("Step 1: Load and Preview Dataset")
try:
    df = pd.read_csv("cleaned_data.csv")
    st.write("### Dataset Overview", df.head())
    st.write("**Dataset Shape:**", df.shape)
    st.write("**Column Names:**", df.columns.tolist())
    st.write("**Data Types:**")
    st.write(df.dtypes)
except Exception as e:
    st.error("Error loading dataset. Make sure 'cleaned_data.csv' exists.")
    st.stop()

# Handling missing values
st.header("Step 2: Handling Missing Values")
st.write("Before handling missing values:")
st.write(df.isnull().sum())

# Filling missing values
if "Apply Date" in df.columns:
    df['Apply Date'].fillna("Not Applied", inplace=True)
    st.write("After handling missing values:")
    st.write(df.isnull().sum())

# Visualizing missing values
st.subheader("Missing Values Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=ax)
st.pyplot(fig)

# Cleaning categorical variables
st.header("Step 3: Cleaning Categorical Variables")
if "Gender" in df.columns and "Current Student Status" in df.columns:
    df['Gender'] = df['Gender'].str.lower().str.strip()
    df['Current Student Status'] = df['Current Student Status'].str.title()
    st.write("Categorical variables cleaned and standardized.")

# Visualizing categorical distributions
st.header("Step 4: Categorical Data Distributions")
col1, col2 = st.columns(2)

with col1:
    if "Gender" in df.columns:
        st.subheader("Gender Distribution")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x='Gender', palette='Set2', ax=ax)
        st.pyplot(fig)

with col2:
    if "Current Student Status" in df.columns:
        st.subheader("Current Student Status Distribution")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x='Current Student Status', palette='Set3', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Relationship between Reward Amount and Skill Points Earned
st.header("Step 5: Relationship Analysis")
if "Reward Amount" in df.columns and "Skill Points Earned" in df.columns:
    st.subheader("Reward Amount vs. Skill Points Earned")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='Reward Amount', y='Skill Points Earned', hue='Gender', palette='Set1', ax=ax)
    st.pyplot(fig)

# Histogram: Reward Amount distribution
st.subheader("Reward Amount Distribution")
if "Reward Amount" in df.columns:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x='Reward Amount', bins=30, kde=True, color='blue', ax=ax)
    st.pyplot(fig)

# Boxplot: Reward Amount by Gender
st.subheader("Reward Amount by Gender")
if "Gender" in df.columns and "Reward Amount" in df.columns:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x='Gender', y='Reward Amount', palette='Set2', ax=ax)
    st.pyplot(fig)

# Pie chart: Gender distribution
st.header("Step 6: Gender Distribution Analysis")
if "Gender" in df.columns:
    gender_counts = df['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen'])
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

# Location analysis
st.header("Step 7: Top 10 Countries by User Count")
if "Country" in df.columns:
    location_counts = df['Country'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=location_counts.index, y=location_counts.values, palette='Set3', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Correlation matrix
st.header("Step 8: Correlation Analysis")
numeric_df = df.select_dtypes(include=['number'])
if numeric_df.shape[1] > 0:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)
else:
    st.write("No numeric columns available for correlation analysis.")

st.success("Exploratory Data Analysis Completed Successfully!")
