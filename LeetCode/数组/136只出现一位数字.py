# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  说明： 
# 
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
# 
#  示例 1: 
# 
#  输入: [2,2,1]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入: [4,1,2,1,2]
# 输出: 4 
#  Related Topics 位运算 哈希表


from typing import List


"""
Python内置count
"""
def singleNumber(nums: List[int]) -> int:
	for i in nums:
		if nums.count(i) == 1:
			return i

"""
hash 会开辟额外空间
"""		
def singleNumber1(nums: List[int]) -> int:
	hash = {}
	for i in nums:
		if hash.get(i) is None:
			hash[i] = 0
		else:
			hash[i] += 1
	for k, v in hash.items():
		if v == 0:
			return k


"""
异或运算 数组中的全部元素的异或运算结果即为数组中只出现一次的数字
"""
def singleNumber2(nums: List[int]) -> int:
	from functools import reduce
	return reduce(lambda x, y : x ^ y, nums)


if __name__ == '__main__':
	nums = [4,1,2,1,2]
	print(singleNumber(nums))
	nums = [2,2,1]
	print(singleNumber(nums))
	nums = [1,0,1]
	print(singleNumber(nums))


	nums = [4,1,2,1,2]
	print(singleNumber1(nums))
	nums = [2,2,1]
	print(singleNumber1(nums))
	nums = [1,0,1]
	print(singleNumber1(nums))
	a ={4: 0, 1: 1, 2: 1}

	nums = [4,1,2,1,2]
	print(singleNumber2(nums))
	nums = [2,2,1]
	print(singleNumber2(nums))
	nums = [1,0,1]
	print(singleNumber2(nums))
	a ={4: 0, 1: 1, 2: 1}