"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


"""
1、先排序，固定一个数，然后使用双指针
2、初始化时，把第一个元素设为固定值，第二个和最后一个元素设置left指针和right指针
3、这样确定了三个数，然后判断相加是否得0，如果固定下来的数本身大于0，那么三数之和一定不等于0，直接返回就可
4、移动指针 如果和大于0，那就说明 right 的值太大，需要左移。如果和小于0，那就说明 left 的值太小，需要右移
5、处理重复值情况。对于 left 和 left+1，以及 right 和 right-1，我们都单独做一下重复值的处理 跳过
"""
def threeSum(nums: List[int]) -> List[List[int]]:
	n = len(nums)
	if not nums or n < 3:
		return []
	nums.sort()
	res = []
	for i in range(n):
		if nums[i] > 0:
			return res
		if(i>0 and nums[i]==nums[i-1]):
			continue
		left = i + 1
		right = n - 1
		while left < right:
			if nums[i] + nums[left] + nums[right] == 0:
				res.append([nums[i], nums[left], nums[right]])
				while(left<right and nums[left]==nums[left+1]):
					left=left+1
				while(left<right and nums[right]==nums[right-1]):
					right=right-1
				left += 1
				right -= 1
			elif nums[i] + nums[left] + nums[right] > 0:
				right -= 1
			else:
				left += 1
	return res



if __name__ == '__main__':
	nums = [-1, 0, 1, 2, -1, -4]
	print(threeSum(nums))