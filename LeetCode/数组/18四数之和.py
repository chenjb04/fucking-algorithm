"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from typing import List


"""
特判，对于数组长度nn，如果数组为Null或者数组长度小于4，返回[][]。
对数组进行排序。
遍历排序后数组：
对于重复元素，跳过，条件：i>0 且 nums[i]==nums[i-1]i>0且nums[i]==nums[i−1]，避免出现重复解
二次遍历，重复元素跳过，判断重复元素从ii后第二个元素开始，所以条件：j-i>1 且 nums[j]==nums[j-1]j−i>1且nums[j]==nums[j−1]
令左指针L=j+1L=j+1,右指针R=n-1R=n−1,当L<RL<R时，执行循环：
*当nums[i]+nums[j]+nums[L]+nums[R]==targetnums[i]+nums[j]+nums[L]+nums[R]==target时,将结果加入resres并执行循环，判断左界和右界是否和下一位置重复，以去除重复解。并同时将L,RL,R移到下一位置，寻找新的解
*若和大于0，说明nums[R]nums[R]太大，RR左移
*若和小于0，说明nums[L]nums[L]太小，LL右移

第一次遍历

若nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>targetnums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target,则可以退出，因为最小四数之和大于目标，则不可能存在结果。**注意：**和三数之和的优化条件不同，三数之和中target=0target=0,所以只要nums[i]>0nums[i]>0,则可退出，这里则需要更为严格的条件。
若当前值和数组中最大的三个值相加依旧小于目标，nums[i] + nums[n- 1] + nums[n- 2] + nums[n- 3] < targetnums[i]+nums[n−1]+nums[n−2]+nums[n−3]<target,则continue
第二次遍历

同理，若nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > targetnums[i]+nums[j]+nums[j+1]+nums[j+2]>target,break
nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < targetnums[i]+nums[j]+nums[n−1]+nums[n−2]<target,continue

"""
def fourSum(nums: List[int], target: int) -> List[List[int]]:
	n = len(nums)
	if not nums or n < 4:
		return []
	nums.sort()
	res = []
	for i in range(n - 3):
		if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
			break
		if nums[i]+nums[-1]+nums[-2]+nums[-3]<target:
			continue
		if i>0 and nums[i]==nums[i-1]:
			continue
		for j in range(i+1, n-2):
			if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target:
				break
			if nums[i]+nums[j]+nums[-1]+nums[-2]<target:
				continue
			if j-i>1 and nums[j]==nums[j-1]:
				continue

			left = j + 1
			right = n - 1

			while left < right:
				if nums[i] + nums[j] + nums[left] + nums[right] == target:
					res.append([nums[i], nums[j],nums[left],nums[right]])
					while(left<right and nums[left]==nums[left+1]):
						left=left+1
					while(left<right and nums[right]==nums[right-1]):
						right=right-1
					left += 1
					right -= 1
				elif nums[i] + nums[j] + nums[left] + nums[right] > target:
					right -= 1
				else:
					left += 1
	return res


if __name__ == '__main__':
	nums = [1, 0, -1, 0, -2, 2]
	target = 0
	print(fourSum(nums, target))