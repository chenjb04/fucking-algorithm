"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List

"""
暴力破解 双层循环
"""
def twoSum(nums: List[int], target: int) -> List[int]:
	for i in range(len(nums) + 1):
		for j in range(i + 1):
			if nums[i] + nums[j] == target and i !=j :
				return [j, i]

"""
优化
"""
def twoSum1(nums: List[int], target: int) -> List[int]:
	for i in range(len(nums) + 1):
		result = target - nums[i]
		if result in nums and nums.index(result) != i:
			return [i, nums.index(result)]


"""
通过迭代将元素添加到哈希表中，同时我们比较该元素的对应元素是否已经存在与哈希表中，如果存在，我们直接返回答案。
"""
def twoSum2(nums: List[int], target: int) -> List[int]:
	hashmap = {}
	for i in range(len(nums)):
		if target - nums[i] in hashmap:
			return [hashmap[target - nums[i]], i]
		else:
			hashmap[nums[i]] = i


if __name__ == '__main__':
	nums =  [3, 2, 4]
	target = 6
	print(twoSum(nums, target))
	print(twoSum1(nums, target))
	print(twoSum2(nums, target))
