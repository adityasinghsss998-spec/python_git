import numpy as np
import pandas as pd
from scipy import stats

# Load dataset
df = pd.read_csv("student_marks.csv")

marks = df["Marks"]

# Mean
mean = np.mean(marks)

# Median
median = np.median(marks)

# Mode
mode = stats.mode(marks, keepdims=True)

# Variance
variance = np.var(marks)

# Standard deviation
std_dev = np.std(marks)

# Quartiles
Q1 = np.percentile(marks, 25)
Q3 = np.percentile(marks, 75)

# IQR
IQR = Q3 - Q1

# Outlier limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify outliers
outliers = marks[(marks < lower_limit) | (marks > upper_limit)]

print("Student Marks:")
print(df)

print("\nMean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0])
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_limit)
print("Upper Bound:", upper_limit)
print("Outliers:", list(outliers))
