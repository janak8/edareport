import pandas as pd

# Load data
df = pd.read_csv('Opportunity Wise Data.csv')
print(f"Initial rows: {len(df)}")

# 1. Explore the Dataset

print("\n=== Initial Data Exploration ===")
print("Structure:")
print(df.info())

# Review data structure, column names, and variable types
print("\nSummary Stats:")
print(df.describe())  # Explore summary statistics
print("\nUnique Values Check:")
print(df.nunique())  # Identify unique values for each column
print("\nMissing Values Before Cleaning:")
print(df.isna().sum())  # Assess missing data

# 2. Handling Missing Values
print("\n=== Handling Missing Values ===")
for col in df.columns:
    if df[col].dtype == 'object':  # For categorical columns
        mode_value = df[col].mode()
        fill_value = mode_value[0] if not mode_value.empty else 'Unknown'
        df[col] = df[col].fillna(fill_value)
        print(f"Filled missing values in '{col}' with '{fill_value}'.")
    else:  # For numeric columns
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
        print(f"Filled missing values in '{col}' with median value '{median_value}'.")

# 3. Address Duplicate Data


print("\n=== Removing Duplicate Data ===")
initial_rows = len(df)
df = df.drop_duplicates()
rows_after_duplicate_removal = len(df)
print(f"Removed {initial_rows - rows_after_duplicate_removal} duplicate rows.")
print(f"Rows after duplicate removal: {rows_after_duplicate_removal}")

# 4. Standardize Formats


print("\n=== Standardizing Formats ===")
date_cols = ['Opportunity End Date', 'Apply Date', 'Opportunity Start Date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')  # Standardize date formats
    print(f"Standardized date format for '{col}'.")

df['Gender'] = df['Gender'].str.lower().str.strip()  # Standardize gender categories
print("Standardized 'Gender' column to lowercase and stripped whitespace.")

# 5. Validate Numeric Data


print("\n=== Validating Numeric Data ===")
numeric_cols = ['Reward Amount', 'Skill Points Earned']
for col in numeric_cols:
    invalid_count = df[df[col] < 0].shape[0]
    df = df[df[col] >= 0]  # Ensure values are non-negative
    print(f"Removed {invalid_count} invalid rows from '{col}' where values were negative.")

# 6. Validate Categorical Data
print("\n=== Validating Categorical Data ===")
valid_genders = ['male', 'female', 'm', 'f', 'other']
invalid_gender_count = df[~df['Gender'].isin(valid_genders)].shape[0]
df = df[df['Gender'].isin(valid_genders)]  # Filter valid gender categories
print(f"Removed {invalid_gender_count} rows with invalid 'Gender' values.")

# 7. Cross-Check Relationships
print("\n=== Cross-Checking Relationships ===")
invalid_date_count = df[df['Opportunity End Date'] < df['Opportunity Start Date']].shape[0]
df = df[df['Opportunity End Date'] >= df['Opportunity Start Date']]  # Ensure logical date relationships
print(f"Removed {invalid_date_count} rows where 'Opportunity End Date' was earlier than 'Opportunity Start Date'.")

# Final Check
print("\n=== Cleaned Data Summary ===")
print(f"Final rows: {len(df)}")
print("\nMissing Values After Cleaning:")
print(df.isna().sum())
print("\nUnique Values Check:")
print(df.nunique())

# 8. Document the Process
print("\n=== Documenting the Process ===")
cleaning_log = f"""
Data Cleaning Log:
1. Initial rows: {len(df)}
2. Removed duplicates: {initial_rows - rows_after_duplicate_removal}
3. Final valid rows: {len(df)}
4. Columns cleaned: {list(df.columns)}
5. Actions Taken:
   - Filled missing values in categorical columns with mode or 'Unknown'.
   - Filled missing values in numeric columns with median.
   - Removed duplicate rows.
   - Standardized date formats and gender categories.
   - Validated numeric columns to ensure non-negative values.
   - Validated categorical columns to ensure consistency.
   - Cross-checked logical relationships between dates.
"""

# Export cleaned data and cleaning log
df.to_csv('cleaned_data.csv', index=False)
with open('cleaning_log.txt', 'w') as f:
    f.write(cleaning_log)

print("\nCleaning complete! Saved cleaned_data.csv and cleaning_log.txt")