import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel('../data/cleaned_data.xlsx')

# Overview
print(df.info())
print(df.describe())
print(df.head())

# Numerical column distributions
num_cols = ['price','quantity','discount','tax','shippingcost']
df[num_cols].hist(bins=20, figsize=(12,8))
plt.tight_layout()
plt.show()

# Categorical columns distribution
cat_cols = ['category','subcategory','region','paymentmethod','orderstatus']
for col in cat_cols:
    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation of Numerical Columns')
plt.show()

# Revenue analysis
df['total_sales'] = df['price']*df['quantity']*(1-df['discount']) + df['tax'] + df['shippingcost']
sales_by_category = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
print("Total Sales by Category:")
print(sales_by_category)

plt.figure(figsize=(8,4))
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
