# Task 1: Write and Read a text file with error handling

try:
    # Writing to a file
    with open("students.txt", "w") as f:
        f.write("Alice 85\n")
        f.write("Bob 90\n")
        f.write("Charlie 78\n")
        f.write("David 92\n")
        f.write("Eva 88\n")

    # Reading from the same file
    with open("students.txt") as f:
        print("Contents of students.txt:\n")
        print(f.read())

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An unexpected error occurred:", e)
