"""

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 

示例: 

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


进阶: 

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
Related Topics 数组 分治算法 动态规划
"""
from typing import List


"""
动态规划
状态转移方程：dp[i] = max(dp[i-1] + nums[i], nums[i])
"""
def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    return max(dp)


if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(maxSubArray(nums))