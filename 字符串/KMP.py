# KMP算法匹配字符串，O(m + n)
# 给定主字符串t和匹配字符串p
class Solution():
	def getNext(self, p):
		self.next = [0] * len(p)
		self.next[0] = -1

		i, j = 0, -1
		while i < len(p) - 1:
			if j == -1 or p[i] == p[j]:
				i += 1
				j += 1
				self.next[i] = j
			else:
				j = self.next[j]

	def KMP(self, t, p):
		self.getNext(p)
		
		i, j = 0, 0
		while i < len(t) and j < len(p):
			if j == -1 or t[i] == p[j]:
				i += 1
				j += 1
			else:
				j = self.next[j]

		if j == len(p):
			return i - j
		else:
			return -1

solution = Solution()
t = "abbaabbaaba"
p = "abbaaba"
print(solution.KMP(t, p))