import numpy as np

data = [10, 12, 15, 18, 20, 22, 25, 30, 35, 40]

# Range
data_range = max(data) - min(data)

# Variance
variance = np.var(data)

# Standard deviation
std_dev = np.std(data)

# Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

# Interquartile Range
IQR = Q3 - Q1

print("Data:", data)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("Interquartile Range (IQR):", IQR)
