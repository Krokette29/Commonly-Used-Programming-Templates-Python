def binarySearch(arr, target):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1


import random
def test():
	arr = [random.randint(0, 10) for _ in range(10)]
	arr.sort()
	target = random.randint(0, 10)

	index = binarySearch(arr, target)
	if index == -1 and target in arr or index != -1 and arr[index] != target:
		raise ValueError("Wrong result! {}, {}, {}".format(arr, target, index))

def main():
	for _ in range(1000):
		test()

	print("Correct!")

if __name__ == "__main__":
	main()
