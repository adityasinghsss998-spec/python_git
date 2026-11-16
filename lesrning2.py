import numpy as np

print(np.empty((4, 4), dtype=int))
x = np.ones(6)
print(x)
y = np.ones((3, 5), dtype=int)
print(y)
a = np.arange(1, 20)
print(a)
a = np.arange(2, 20, 2)
print(a)
a = a.reshape((3, 3))
print(a)
b = a.ravel()
print(b)
a = a.flatten()
print(a)

# ravel returns only reference of original aray so value changes in orginnal too
# faltten return only copy so oringinal array doesnot changes aslo ravel is faster
a = np.arange(1, 51)
a = a.reshape(10, 5)
print(a)
print(a[0])
print(a[0][0])
print(a[5:10])
print(a[:, 2])
print(a[2:5, 4])
