from Tree import *

def preorderDFS_iterative(root: Node):
	if not root: return []

	res = []
	stack = [root]
	while stack:
		pop = stack.pop()
		res.append(pop.val)
		if pop.right: stack.append(pop.right)
		if pop.left: stack.append(pop.left)

	return res


def preorderDFS_recursion(root: Node):
	if not root: return []

	res = []
	def dfs(node):
		res.append(node.val)
		if node.left: dfs(node.left)
		if node.right: dfs(node.right)

	dfs(root)
	return res


tree = Tree([i for i in range(1, 8)])
res1 = preorderDFS_iterative(tree.root)
res2 = preorderDFS_recursion(tree.root)
tree.draw()
print("preorder using stack: \t\t", res1)
print("preorder using recursion: \t", res2)
