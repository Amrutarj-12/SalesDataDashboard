import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Step 1: Load Dataset
# ---------------------------
# Example CSV data format:
# Product,Quantity,Price,Region
# Laptop,5,60000,North
# Mobile,10,15000,South
# Headphones,15,2000,East
# Laptop,3,60000,West

df = pd.read_csv("sales_data.csv")
print("📊 Sales Dataset:")
print(df.head())

# ---------------------------
# Step 2: Calculate Revenue
# ---------------------------
df["Revenue"] = df["Quantity"] * df["Price"]
total_revenue = df["Revenue"].sum()
print(f"\n💰 Total Revenue: {total_revenue}")

# ---------------------------
# Step 3: Top Products by Revenue
# ---------------------------
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n🏆 Top Products by Revenue:")
print(top_products)

# ---------------------------
# Step 4: Sales by Region
# ---------------------------
sales_by_region = df.groupby("Region")["Revenue"].sum()
print("\n🌍 Sales by Region:")
print(sales_by_region)

# ---------------------------
# Step 5: Visualization
# ---------------------------

# Bar Chart – Top Products by Revenue
top_products.plot(kind="bar", color="skyblue", title="Top Products by Revenue")
plt.ylabel("Revenue")
plt.show()

# Pie Chart – Sales by Region
sales_by_region.plot(kind="pie", autopct="%1.1f%%", startangle=140, title="Sales by Region")
plt.ylabel("")  # Remove y-label
plt.show()