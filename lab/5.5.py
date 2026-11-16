# Task 5: Print frequency of each unique word in sorted order

try:
    with open("data.txt") as f:
        text = f.read().lower()

    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print("Word Frequencies (sorted):")
    for word in sorted(freq):
        print(f"{word}: {freq[word]}")

except FileNotFoundError:
    print("Error: data.txt not found.")
