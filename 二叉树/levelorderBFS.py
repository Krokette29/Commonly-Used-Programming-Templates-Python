from Tree import *
from collections import deque

def BFS_solution1(root: Node):
	if not root: return [], 0

	res = [[]]
	layer = 0
	queue = deque()
	queue.append(root)
	while len(queue) != 0:
		for _ in range(len(queue)):
			pop = queue.popleft()
			res[layer].append(pop.val)
			if pop.left: queue.append(pop.left)
			if pop.right: queue.append(pop.right)

		layer += 1
		res.append([])

	return res[:-1], layer


def BFS_solution2(root: Node):
	if not root: return [], 0

	res = []
	layer = 0
	queue = deque()
	queue.append(root)
	queue.append(None)
	tmp = []
	while len(queue) != 0:
		pop = queue.popleft()
		if pop == None:
			if len(queue) != 0: queue.append(None)
			res.append(tmp)
			tmp = []
			layer += 1

		else:
			tmp.append(pop.val)
			if pop.left: queue.append(pop.left)
			if pop.right: queue.append(pop.right)

	return res, layer

tree = Tree([i for i in range(1, 8)])
res, layer = BFS_solution1(tree.root)
tree.draw()
print("BFS using queue: \t", res)
print("layer of the tree: \t", layer)
