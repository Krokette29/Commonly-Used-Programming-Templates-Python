from Tree import *
from collections import deque

def BFS(root: Node):
	if not root: return []

	res = []
	layer = 0
	queue = deque()
	queue.append(root)
	queue.append(None)
	while len(queue) != 0:
		pop = queue.popleft()
		if pop == None:
			if len(queue) != 0: queue.append(None)
			layer += 1

		else:
			res.append(pop.val)
			if pop.left: queue.append(pop.left)
			if pop.right: queue.append(pop.right)

	return res, layer


tree = Tree([i for i in range(1, 8)])
res, layer = BFS(tree.root)
tree.draw()
print("BFS using queue: \t", res)
print("layer of the tree: \t", layer)
