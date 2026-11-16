# Task 3: Count lines, words, and characters in a file

try:
    with open("sample.txt") as f:
        lines = f.readlines()

        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

    print("File Statistics for sample.txt:")
    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")

except FileNotFoundError:
    print("sample.txt not found.")
