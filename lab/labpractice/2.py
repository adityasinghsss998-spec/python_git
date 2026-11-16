for i in range(1, 13):
    print(f"{i:4}", end=" ")
print("\n" + "-" * 52)
for i in range(1, 13):
    print(f" {i:2} | ", end=" ")
    for j in range(1, 13):
        ele = i * j
        print(f"{ele: 4}", end=" ")
    print()
