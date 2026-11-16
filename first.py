fruits = ["apple", "banana", "cherry"]
fruits2 = ["anna", "vdvdd"]
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.append("guava")
print(fruits)
fruits.insert(8, "naa")
print(fruits)
fruits.extend(fruits2)
print(fruits)
print(fruits2)
fruits2.clear()
print(fruits2)
nums = [43, 2, 24, 4, 2]
nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)
a = [1, 2, 3]
b = a.copy()
# shallow copy
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
a.remove(2)
print(a)
l = [1, 2, "aditya"]
print(l.pop())
print(l)
