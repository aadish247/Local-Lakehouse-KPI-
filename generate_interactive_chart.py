import pandas as pd
import plotly.express as px

# Sample data for relationships
fact_sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [1000, 1500, 2000, 2500],
    'Product': ['A', 'B', 'C', 'D']
})

dim_customer = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
    'Purchases': [5, 3, 8, 2],
    'Month': ['Jan', 'Feb', 'Mar', 'Apr']
})

dim_product = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Revenue': [5000, 3000, 4000, 2000],
    'Category': ['Electronics', 'Furniture', 'Clothing', 'Books']
})

# Merge data for relationships
merged_data = pd.merge(fact_sales, dim_product, on='Product')
merged_data = pd.merge(merged_data, dim_customer, on='Month')

# Create an interactive chart
fig = px.scatter(
    merged_data,
    x='Sales',
    y='Revenue',
    size='Purchases',
    color='Category',
    hover_name='Customer',
    animation_frame='Month',
    title='Detailed KPI Visualization'
)

# Save the chart as an HTML file
fig.write_html('interactive_chart.html')

print("Interactive chart generated and saved as HTML file.")
