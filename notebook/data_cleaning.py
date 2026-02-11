import pandas as pd
import numpy as np

# Load raw data
df = pd.read_excel('../data/amazon_data.xlsx')

# Inspect data
print("Initial data info:")
print(df.info())
print(df.head())

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Handle missing values
df['customerid'].fillna('UNKNOWN', inplace=True)
df['customername'].fillna('UNKNOWN', inplace=True)
df['quantity'].fillna(1, inplace=True)
df['discount'].fillna(0, inplace=True)

# Convert numeric columns safely
# Remove unwanted characters
df['price'] = df['price'].replace({r'\$': '', 'USD': '', ',': ''}, regex=True)
df['discount'] = df['discount'].replace({'%': '', ',': ''}, regex=True)
df['tax'] = df['tax'].replace({r'\$': '', 'USD': '', ',': ''}, regex=True)
df['shippingcost'] = df['shippingcost'].replace({r'\$': '', 'USD': '', ',': ''}, regex=True)

# Convert to numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')
df['tax'] = pd.to_numeric(df['tax'], errors='coerce')
df['shippingcost'] = pd.to_numeric(df['shippingcost'], errors='coerce')

# Calculate tax if missing
df['tax'] = df['tax'].fillna(df['price'] * 0.1)

# Convert orderdate to datetime
df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce', dayfirst=True)

# Clean text fields
text_cols = ['region', 'category', 'subcategory', 'paymentmethod']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# Remove duplicates
df.drop_duplicates(subset=['orderid'], inplace=True)

# Correct negative prices and quantities
df.loc[df['price'] < 0, 'price'] = np.nan
df['price'].fillna(df['price'].median(), inplace=True)

df.loc[df['quantity'] < 0, 'quantity'] = 1

# Calculate total_sales
# total_sales = (price * quantity * (1 - discount/100)) + tax + shippingcost
df['total_sales'] = (df['price'] * df['quantity'] * (1 - df['discount']/100)) + df['tax'] + df['shippingcost']

# Save cleaned data
df.to_excel('../data/cleaned_data.xlsx', index=False)
print("Data cleaning complete. Cleaned file saved as 'cleaned_data.xlsx'.")
