import pandas as pd
import plotly.express as px

# Creating a Sample Dataset
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}
df = pd.DataFrame(data)

# Bar Chart - Sales by Product
fig = px.bar(df, x='Product', y='Sales',
             title='Sales by Product')
fig.show()

# Line Chart - Profit by Product
fig = px.line(df, x='Product', y='Profit',
              title='Profit by Product')
fig.show()

# Scatter Plot - Sales vs Profit
fig = px.scatter(df, x='Sales', y='Profit',
                 color='Product',
                 title='Sales vs Profit')
fig.show()

# Enhanced Bar Chart
fig = px.bar(df, x='Product', y='Sales',
             title='Sales by Product (Enhanced)',
             color='Profit',
             text='Sales')

fig.update_layout(
    xaxis_title='Product',
    yaxis_title='Sales',
    legend_title='Profit',
    template='plotly_dark'
)
fig.show()

# Exporting Visualizations
# Save as HTML
fig.write_html('sales_by_product.html')
# Save as PNG (Requires kaleido installed)
fig.write_image('sales_by_product.png')
