import numpy as np

a = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 7]])
print(a)
print(a.size)
a = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 7], [5, 6, 7, 8.9, 9]])
print(a)
print(a.size)
print(a.shape)
print(a.dtype)
print(a.transpose())
