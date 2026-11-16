# Function to find student with highest grade


def highest_grade(grades):
    top_student = max(grades, key=grades.get)
    return top_student, grades[top_student]


print("Task 4: Highest Grade")
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
print(highest_grade(students))
