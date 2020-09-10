# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法
from typing import List


"""
hash
"""
def majorityElement(nums: List[int]) -> int:
	n = len(nums)
	hash = {}
	for i in nums:
		if hash.get(i) is None:
			hash[i] = 1

		else:
			hash[i] += 1
	for k, v in hash.items():
		if v > n / 2:
			return k 


if __name__ == '__main__':
	nums = [3,2,3]
	print(majorityElement(nums))
	nums = [2,2,1,1,1,2,2]
	print(majorityElement(nums))