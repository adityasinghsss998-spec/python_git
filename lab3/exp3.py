import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("supermarket_sales_exp3.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Display number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display information about dataset
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nDescriptive Statistics:")
print(df.describe())

# Mean sales
print("\nMean Total Sales:")
print(np.mean(df["Total_Sales"]))

# Median sales
print("\nMedian Total Sales:")
print(np.median(df["Total_Sales"]))

# Standard deviation
print("\nStandard Deviation of Sales:")
print(np.std(df["Total_Sales"]))

# Total sales
print("\nTotal Sales:")
print(df["Total_Sales"].sum())

# Average quantity sold
print("\nAverage Quantity Sold:")
print(df["Quantity"].mean())

# Sales by category
print("\nSales by Category:")
print(df.groupby("Category")["Total_Sales"].sum())

# Sales by city
print("\nSales by City:")
print(df.groupby("City")["Total_Sales"].sum())


# ---------------- HISTOGRAM ----------------

plt.figure(figsize=(8, 5))

plt.hist(df["Total_Sales"], bins=10)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.show()


# ---------------- BOX PLOT ----------------

plt.figure(figsize=(8, 5))

plt.boxplot(df["Total_Sales"])

plt.title("Box Plot of Total Sales")
plt.ylabel("Total Sales")

plt.show()


# ---------------- BAR CHART ----------------

category_sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))

plt.bar(category_sales.index, category_sales.values)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()


# ---------------- CITY SALES ----------------

city_sales = df.groupby("City")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))

plt.bar(city_sales.index, city_sales.values)

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.show()
