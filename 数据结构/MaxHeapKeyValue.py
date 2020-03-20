import heapq
import random
class MaxHeap(object):
	def __init__(self, arr):
		self.arr = [(-item[0], item[1]) for item in arr]
		heapq.heapify(self.arr)

	def heappush(self, item):
		heapq.heappush(self.arr, (-item[0], item[1]))

	def heappop(self):
		pop = heapq.heappop(self.arr)
		return (-pop[0], pop[1])

	def heap(self):
		return [(-item[0], item[1]) for item in self.arr]


def main():
	arr = [(2, 'a'), (5, 'b'), (1, 'c'), (7, 'd'), (9, 'e')]
	print("List: \t", arr)

	heap = MaxHeap(arr)
	print("Heap: \t", heap.heap())

	item = (10, 'f')
	heap.heappush(item)
	print("Push ", item)
	print("Heap: \t", heap.heap())

	print("Pop ", heap.heappop())
	print("Heap: \t", heap.heap())


if __name__ == "__main__":
	main()
