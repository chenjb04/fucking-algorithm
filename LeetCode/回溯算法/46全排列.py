 # 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(path, nums):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path[:], nums[:i] + nums[i+1:])
                path.pop()
        backtrack([], nums)
        return res