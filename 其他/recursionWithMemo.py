def recursionWithMemo(input):
	dp = {}
	def recursion(key):
		if key not in dp:
			dp[key] = someThing

		return dp[key]

	return recursion(input)