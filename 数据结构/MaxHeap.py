import heapq
import random
class MaxHeap(object):
	def __init__(self, arr):
		self.arr = [-i for i in arr]
		heapq.heapify(self.arr)

	def heappush(self, item):
		heapq.heappush(self.arr, -item)

	def heappop(self):
		return -heapq.heappop(self.arr)

	def heap(self):
		return [-i for i in self.arr]


def main():
	arr = [random.randint(0, 10) for _ in range(10)]
	print("List: \t", arr)

	heap = MaxHeap(arr)
	print("Heap: \t", heap.heap())

	item = random.randint(0, 15)
	heap.heappush(item)
	print("Push ", item)
	print("Heap: \t", heap.heap())

	print("Pop ", heap.heappop())
	print("Heap: \t", heap.heap())


if __name__ == "__main__":
	main()
