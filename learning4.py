import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")
print(np.pi)
print(np.sin(np.pi / 2))  # 90 degree
print(np.tan(0))
x = np.arange(1, 11)
y = np.arange(10, 110, 10)
plt.figure(figsize=(6, 6))
plt.plot(x, y, "r--")
plt.show()
x_sin = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x_sin)
print(y_sin)
plt.figure(figsize=(6, 6))
plt.plot(x_sin, y_sin)
plt.title("Sin Curve")
plt.show()
