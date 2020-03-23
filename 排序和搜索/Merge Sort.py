def mergeSort(arr):
	if len(arr) == 1: return arr

	left = mergeSort(arr[:len(arr) // 2])
	right = mergeSort(arr[len(arr) // 2:])

	i, j = 0, 0
	merge = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			merge.append(left[i])
			i += 1
		else:
			merge.append(right[j])
			j += 1

	if i == len(left): merge += right[j:]
	if j == len(right): merge += left[i:]
	return merge