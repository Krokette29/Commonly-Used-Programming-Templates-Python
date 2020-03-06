from collections import deque

class Node(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Tree(object):
	def __init__(self, li):
		self.li = []
		self.root = None
		for i in range(len(li)):
			node = None if not li[i] else Node(li[i])
			self.li.append(node)

			if i == 0:
				self.root = node
			else:
				try:
					parentIndex = (i + 1) // 2 - 1
					if (i + 1) % 2 == 0:
						self.li[parentIndex].left = node
					else:
						self.li[parentIndex].right = node

				except:
					raise ValueError("Cannot create such a tree!")

	def draw(self):
		print("================")
		queue = deque()
		queue.append(self.root)
		queue.append(None)
		string = ""

		while len(queue) != 0:
			pop = queue.popleft()
			if pop == None:
				if len(queue) != 0: queue.append(None)
				print(string)
				string = ""
			else:
				string += "{}\t".format(pop.val)

				if pop.left: queue.append(pop.left)
				if pop.right: queue.append(pop.right)
		print("================")
