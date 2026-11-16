import math

a, b, c = map(float, input("enter the sidesm a,b,c : ").split())
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
A = math.degrees(math.acos((b**2 + c**2 - a**2) / 2 * b * c))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / 2 * a * c))
C = 180 - A - B
print("perimeter : ", a + b + c)
print(area)
print("angles A is : ", A, "B = ", B, "C=", C)
