def binarySearchLeft(arr, target):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return left


def binarySearchRight(arr, target):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] <= target:
			left = mid + 1
		else:
			right = mid - 1
	return left


import bisect
import random
def testLeft(arr, target):
	index = binarySearchLeft(arr, target)
	ans = bisect.bisect_left(arr, target)
	if index != ans:
		raise ValueError("Wrong result! {}, {}".format(arr, target))

def testRight(arr, target):
	index = binarySearchRight(arr, target)
	ans = bisect.bisect_right(arr, target)
	if index != ans:
		raise ValueError("Wrong result! {}, {}, {}, {}".format(arr, target, index, ans))

def main():
	for _ in range(1000):
		arr = [random.randint(0, 10) for _ in range(10)]
		arr.sort()
		target = random.randint(0, 10)

		testLeft(arr, target)
		testRight(arr, target)

	print("Correct!")

if __name__ == "__main__":
	main()
