import random
def quickSort(arr, left, right):
	if left >= right: return None

	index = random.randint(left, right)
	arr[index], arr[right] = arr[right], arr[index]
	pivot = arr[right]

	i = left - 1
	for j in range(left, right + 1):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	quickSort(arr, left, i - 1)
	quickSort(arr, i + 1, right)