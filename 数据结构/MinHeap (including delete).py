import heapq

def MinHeapDelete(arr, item):
	if arr[-1] == item: return arr[:-1]

	for index, value in enumerate(arr):
		if value == item:
			leaf = arr.pop()
			arr[index] = leaf

			if item < leaf:
				heapq._siftup(arr, index)
			else:
				heapq._siftdown(arr, 0, index)

	return arr


def main():
	arr = [3, 2, 1]
	heapq.heapify(arr)
	print(arr)
	heapq.heappush(arr, 0)
	print(arr)
	arr = MinHeapDelete(arr, 0)
	print(arr)


if __name__ == "__main__":
	main()
