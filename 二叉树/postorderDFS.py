from Tree import *

def postorderDFS_iterative(root: Node):
	if not root: return []

	res = []
	stack = [root]
	while stack:
		pop = stack.pop()
		res.append(pop.val)
		if pop.left: stack.append(pop.left)
		if pop.right: stack.append(pop.right)

	res = list(reversed(res))
	return res


def postorderDFS_recursion(root: Node):
	if not root: return []

	res = []
	def dfs(node):
		if node.left: dfs(node.left)
		if node.right: dfs(node.right)
		res.append(node.val)

	dfs(root)
	return res


tree = Tree([i for i in range(1, 8)])
res1 = postorderDFS_iterative(tree.root)
res2 = postorderDFS_recursion(tree.root)
tree.draw()
print("postorder using stack: \t\t", res1)
print("postorder using recursion: \t", res2)
