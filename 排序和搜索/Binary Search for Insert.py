# bisect.bisect_left(arr, target)
def binarySearchLeft(arr, target):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return left

# bisect.bisect_right(arr, target)
def binarySearchRight(arr, target):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] <= target:
			left = mid + 1
		else:
			right = mid - 1
	return left