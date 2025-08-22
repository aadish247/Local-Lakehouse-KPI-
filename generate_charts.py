import matplotlib.pyplot as plt
import pandas as pd

# Sample data for charts
fact_sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [1000, 1500, 2000, 2500]
})

dim_customer = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
    'Purchases': [5, 3, 8, 2]
})

dim_product = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Revenue': [5000, 3000, 4000, 2000]
})

# Generate charts
plt.figure(figsize=(8, 6))
plt.bar(fact_sales['Month'], fact_sales['Sales'], color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('fact_sales_chart.jpg')

plt.figure(figsize=(8, 6))
plt.bar(dim_customer['Customer'], dim_customer['Purchases'], color='orange')
plt.title('Customer Purchases')
plt.xlabel('Customer')
plt.ylabel('Purchases')
plt.savefig('dim_customer_chart.jpg')

plt.figure(figsize=(8, 6))
plt.bar(dim_product['Product'], dim_product['Revenue'], color='green')
plt.title('Product Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.savefig('dim_product_chart.jpg')

print("Charts generated and saved as JPG files.")
