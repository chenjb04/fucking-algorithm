from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
	return [i for i in range(1, len(nums) + 1) if i not in set(nums)]


def findDisappearedNumbers1(nums: List[int]) -> List[int]:
	for num in nums:
		nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
	return [idx + 1 for idx, num in enumerate(nums) if num > 0]


if __name__ == '__main__':
	nums = [4,3,2,7,8,2,3,1]
	print(findDisappearedNumbers(nums))
	print(findDisappearedNumbers1(nums))
