import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel('../data/cleaned_data.xlsx')

#Top 10 products by quantity sold
top_products = df.groupby('productname')['quantity'].sum().sort_values(ascending=False).head(10)
print("Top 10 Products by Quantity Sold:")
print(top_products)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.index, y=top_products.values, palette="viridis")
plt.xticks(rotation=45)
plt.title('Top 10 Products by Quantity Sold')
plt.ylabel('Quantity Sold')
plt.tight_layout()
plt.show()

#Revenue by region 
revenue_by_region = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,4))
revenue_by_region.plot(kind='bar', color='orange')
plt.title('Revenue by Region')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

#Payment method distribution
payment_counts = df['paymentmethod'].value_counts()
plt.figure(figsize=(6,4))
payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Payment Method Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

#Correlation matrix
corr = df[['price','quantity','discount','tax','shippingcost','total_sales']].corr()
print("Correlation Matrix:")
print(corr)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

#Monthly sales trend
df['month'] = df['orderdate'].dt.to_period('M')
monthly_sales = df.groupby('month')['total_sales'].sum()
print("Monthly Sales Trend:")
print(monthly_sales)

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o', linestyle='-', color='green')
plt.title('Monthly Sales Trend')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Revenue by Category and Region (Heatmap)
cat_region_sales = df.pivot_table(values='total_sales', index='category', columns='region', aggfunc='sum', fill_value=0)
plt.figure(figsize=(10,6))
sns.heatmap(cat_region_sales, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Revenue by Category and Region')
plt.tight_layout()
plt.show()

#Discount impact analysis
plt.figure(figsize=(8,4))
sns.scatterplot(data=df, x='discount', y='total_sales', hue='category', alpha=0.7)
plt.title('Discount vs Total Sales')
plt.xlabel('Discount')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

#Top customers by revenue
top_customers = df.groupby('customername')['total_sales'].sum().sort_values(ascending=False).head(10)
print("Top 10 Customers by Revenue:")
print(top_customers)

plt.figure(figsize=(10,5))
sns.barplot(x=top_customers.index, y=top_customers.values, palette="magma")
plt.xticks(rotation=45)
plt.title('Top 10 Customers by Revenue')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

#Upsell / Recommendation logic
# Products with high quantity but low revenue -> suggest upsell
low_revenue_products = df.groupby('productname').apply(lambda x: pd.Series({
    'total_quantity': x['quantity'].sum(),
    'total_revenue': x['total_sales'].sum()
}))
upsell_opportunities = low_revenue_products[
    (low_revenue_products['total_quantity']>50) & 
    (low_revenue_products['total_revenue']<5000)
].sort_values('total_quantity', ascending=False)
print("Upsell Opportunities (High quantity, low revenue products):")
print(upsell_opportunities)

#Recommendation summary
if not upsell_opportunities.empty:
    print("\nRecommendation: Promote these products with bundle deals or cross-selling to increase revenue.")
else:
    print("\nNo immediate upsell opportunities identified based on current data.")
