""""""

from typing import List


def moveZeroes(nums: List[int]) -> None:
	if not nums:
		return
	for i in nums:
		if i == 0:
			nums.remove(0)
			nums.append(0)
	return nums


def moveZeroes1(nums: List[int]) -> None:
	if not nums:
		return
	n = len(nums)
	for i in range(n):
		for j in range(i+1, n):
			if nums[i] == 0:
				nums[i], nums[j] = nums[j], nums[i]
	return nums


if __name__ == '__main__':
	# nums = [0,1,0,3,12]
	# print(moveZeroes(nums))
	# nums = [0,0,0,0,0,1]
	# print(moveZeroes(nums))


	nums = [0,1,0,3,12]
	print(moveZeroes1(nums))
	nums = [0,0,0,0,0,1]
	print(moveZeroes1(nums))