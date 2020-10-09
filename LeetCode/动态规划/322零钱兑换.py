# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 231 - 1 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
def coinChange(coins, amount: int) -> int:
	dp = [float('inf')] * (amount + 1)
	dp[0] = 0
	for i in range(1, amount + 1):
		for coin in coins:
			if i >= coin:
				dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp[-1] if dp[-1] != float('inf') else -1

