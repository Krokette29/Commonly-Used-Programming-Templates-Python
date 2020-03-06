from Tree import *

def inorderDFS_iterative(root: Node):
	if not root: return []

	res = []
	stack = []
	node = root
	while stack or node:
		while node:
			stack.append(node)
			node = node.left

		node = stack.pop()
		res.append(node.val)
		node = node.right

	return res


def inorderDFS_recursion(root: Node):
	if not root: return []

	res = []
	def dfs(node):
		if node.left: dfs(node.left)
		res.append(node.val)
		if node.right: dfs(node.right)

	dfs(root)
	return res


tree = Tree([i for i in range(1, 8)])
res1 = inorderDFS_iterative(tree.root)
res2 = inorderDFS_recursion(tree.root)
tree.draw()
print("inorder using stack: \t\t", res1)
print("inorder using recursion: \t", res2)
