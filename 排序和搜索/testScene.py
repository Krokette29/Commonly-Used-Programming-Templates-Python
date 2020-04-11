import random
arr = [random.randint(0, 10) for _ in range(10)]
print("Before sorting: \t", arr)

arr = mergeSort(arr)
print("After sorting: \t\t", arr)
print("Result: \t\t\t", sorted(arr))
