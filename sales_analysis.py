import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sales dataset
df = pd.read_csv("flipkart_sales.csv")  # Make sure the CSV is in the same folder
print("First 5 rows of the dataset:")
print(df.head())

# Clean the data
df.columns = df.columns.str.strip()  # Remove spaces in column names
# Step 6: Convert 'Order Date' column to proper datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Optional: Format date for Excel display (as YYYY-MM-DD)
df['Order Date'] = df['Order Date'].dt.strftime('%Y-%m-%d')

print("\nMissing values:\n", df.isnull().sum())  # Check for missing data
df = df.dropna()  # Drop rows with missing values

# Convert columns to float by removing ₹ and ,
df['Price (INR)'] = df['Price (INR)'].replace('[₹,]', '', regex=True).astype(float)
df['Total Sales (INR)'] = df['Total Sales (INR)'].replace('[₹,]', '', regex=True).astype(float)

# Analyze top-selling products
top_products = df.groupby('Product Name')['Total Sales (INR)'].sum()
top_products = top_products.sort_values(ascending=False).head(10)
print("\nTop 10 Best Selling Products by Total Sales:")
print(top_products)

# Visualize the top-selling products
plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='coolwarm')
plt.title("Top 10 Best Selling Products by Total Sales")
plt.xlabel("Total Sales (INR)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

#Export cleaned data
df.to_csv('cleaned_flipkart_sales.csv', index=False)
print("Cleaned data saved as 'cleaned_flipkart_sales.csv'")