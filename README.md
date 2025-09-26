## Sales Data Analysis Project

* Overview
This project analyzes sales data from a CSV file and provides insights into total revenue, top-performing products, and sales distribution across regions.
It uses Python, Pandas, and Matplotlib for data analysis and visualization.

##Features

1.Load and clean sales data from CSV.

2.Calculate total revenue.

3.Identify top products by revenue.

4.Analyze sales by region.

5.Visualize insights with bar charts and pie charts.

##Dataset Format

The dataset should be in CSV format, for example:

Product,Quantity,Price,Region
Laptop,5,60000,North
Mobile,10,15000,South
Headphones,15,2000,East
Laptop,3,60000,West


1.Product → Name of the product

2.Quantity → Units sold

3.Price → Price per unit

4.Region → Sales region

## How It Works

Load Dataset

Reads the CSV file using Pandas.

Calculate Revenue

Adds a new column:

Revenue = Quantity × Price


Calculates total revenue.

Top Products by Revenue

Groups data by Product.

Sorts products by revenue (highest → lowest).

Sales by Region

Groups data by Region.

Shows revenue contribution of each region.

##Visualization

Bar Chart → Top products by revenue.

Pie Chart → Sales distribution by region.

## Example Visualizations
🔹 Top Products by Revenue (Bar Chart)

Shows which products generate the most revenue.

🔹 Sales by Region (Pie Chart)

Displays the revenue share of each region.

## Technologies Used

Python

Pandas – Data analysis

Matplotlib – Data visualization

##Insights You Can Get

Which products are most profitable?

Which region contributes the most to revenue?

What is the overall sales performance?

## With this project, businesses can track performance, identify best-sellers, and plan regional strategies effectively.
