class UFS(object):
	def __init__(self, length):
		self.p = [i for i in range(length)]
		self.rank = [0 for _ in range(length)]

	def find(self, x):
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
		return self.p[x]

	def union(self, x, y):
		rx, ry = self.find(x), self.find(y)
		if self.rank[rx] < self.rank[ry]:
			self.p[rx] = ry
		elif self.rank[rx] > self.rank[ry]:
			self.p[ry] = rx
		else:
			self.p[rx] = ry
			self.rank[ry] += 1
