import heapq

def MaxHeapHeapify(arr):
	heapq._heapify_max(arr)
	return arr


def MaxHeapPush(arr, item):
	arr.append(item)
	heapq._siftdown_max(arr, 0, len(arr) - 1)
	return arr


def MaxHeapDelete(arr, item):
	if arr[-1] == item: return arr[:-1]

	for index, value in enumerate(arr):
		if value == item:
			leaf = arr.pop()
			arr[index] = leaf

			if item > leaf:
				heapq._siftup_max(arr, index)
			else:
				heapq._siftdown_max(arr, 0, index)

	return arr


def main():
	arr = [1, 2, 3]
	print(MaxHeapHeapify(arr))
	print(MaxHeapPush(arr, 4))
	print(MaxHeapDelete(arr, 4))


if __name__ == "__main__":
	main()
	