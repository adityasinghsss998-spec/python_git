# Function to find sum, average and max of a list


def list_summary(nums):
    total = sum(nums)
    avg = total / len(nums)
    maximum = max(nums)
    return total, avg, maximum


print("Task 2: List Summary")
lst = [10, 20, 30, 40, 50]
print(list_summary(lst))
