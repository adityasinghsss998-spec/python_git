# Rectangle area and perimeter function
def rectangle_area_perimeter(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter


print("Task 1: Rectangle Area and Perimeter")
print(rectangle_area_perimeter(5, 3))
print(rectangle_area_perimeter(10, 7))
print(rectangle_area_perimeter(8, 8))
