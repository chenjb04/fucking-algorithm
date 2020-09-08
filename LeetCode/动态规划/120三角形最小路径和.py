"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。 



例如，给定三角形： 

[
 [2],
[3,4],
[6,5,7],
[4,1,8,3]
]


自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 



说明： 

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
Related Topics 数组 动态规划

"""
from typing import List


"""
动态规划
状态转移方程：dp[i] = cur[i] + min(dp[i] + dp[i+1])
"""
def minimumTotal(triangle: List[List[int]]) -> int:
	# 把最后一行当做初始化dp数组
	dp = triangle[-1]
	# 从倒数第二层开始遍历
	for i in range(len(triangle) - 2, -1, -1):
		# 遍历每层的位置
		for j in range(i + 1):
			dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
	print(dp)
	return dp[0]


if __name__ == '__main__':
	triangle = [
				[2],
				[3,4],
				[6,5,7],
				[4,1,8,3]
				]
	print(minimumTotal(triangle))