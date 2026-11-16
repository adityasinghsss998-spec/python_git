import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("employee_salary.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Select salary column
salary = df["Salary"]

# Mean
print("\nMean Salary:", np.mean(salary))

# Median
print("Median Salary:", np.median(salary))

# Variance
print("Variance:", np.var(salary))

# Standard Deviation
print("Standard Deviation:", np.std(salary))

# Minimum and Maximum
print("Minimum Salary:", np.min(salary))
print("Maximum Salary:", np.max(salary))

# Range
print("Salary Range:", np.max(salary) - np.min(salary))

# Quartiles
Q1 = np.percentile(salary, 25)
Q2 = np.percentile(salary, 50)
Q3 = np.percentile(salary, 75)

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

# IQR
IQR = Q3 - Q1

print("IQR:", IQR)


# ---------------- HISTOGRAM ----------------

plt.figure(figsize=(8, 5))

plt.hist(salary, bins=10)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()


# ---------------- BOX PLOT ----------------

plt.figure(figsize=(8, 5))

plt.boxplot(salary)

plt.title("Box Plot of Employee Salaries")
plt.ylabel("Salary")

plt.show()


# ---------------- BAR CHART ----------------

department_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5))

plt.bar(department_salary.index, department_salary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()
