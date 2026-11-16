# Task 4: Copy contents of source.txt into destination.txt

try:
    with open("source.txt") as src:
        data = src.read()

    with open("destination.txt", "w") as dest:
        dest.write(data)

    print("Contents copied successfully from source.txt to destination.txt")

except FileNotFoundError:
    print("Error: source.txt not found.")
