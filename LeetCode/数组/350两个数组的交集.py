# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 
#  我们可以不考虑输出结果的顺序。 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
#  Related Topics 排序 哈希表 双指针 二分查找
from typing import List

"""
方法一：暴力破解
思路：
	把短的数组放在前面
	循环短的数组，判断值是否在第二个数组中，在就加入临时数组，并把第二个数组中的值移除
	返回临时数组
"""
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
 	temp = []
 	if len(nums1) > len(nums2):
 		nums1, nums2 = nums2, nums1
 	for i in nums1:
 		if i in nums2:
 			temp.append(i)
 			nums2.remove(i)
 	return temp


"""
方法二：哈希映射
思路：
	循环第一个数组，记录数字出现的次数
	循环第二个数组，如果数字大于0，添加到临时数组

"""
def intersect1(nums1: List[int], nums2: List[int]) -> List[int]:
	dic = {}
	temp = []
	for i in nums1:
		dic[i] = dic.get(i, 0) + 1
	for j in nums2:
		try:
			if dic[j] > 0:
				temp.append(j)
				dic[j] -= 1
		except Exception as e:
			continue
	return temp


"""
方法三：双指针
思路：
	定义两个从零开始的指针，比较两个元素指针是否相等
	如果第一个指针元素小于第二个指针元素，那么把第一个指针前移一位
	如果第一个指针元素等于第二个指针元素，那么把第一个指针元素添加到临时列表，双指针都前移一位
	如果第一个指针元素大于第二个指针元素，那么把第二个指针前移一位
"""
def intersect2(nums1: List[int], nums2: List[int]) -> List[int]:
	nums1.sort()
	nums2.sort()
	first = 0
	second = 0
	res = []
	while first < len(nums1) and second < len(nums2):
		if nums1[first] < nums2[second]:
			first += 1
		elif nums1[first] == nums2[second]:
			res.append(nums1[first])
			first += 1
			second += 1
		else:
			second += 1
	return res



if __name__ == '__main__':
	# nums1 = [4,9,5]
	# nums2 = [9,4,9,8,4]
	nums1 = [3,1,2]
	nums2 = [1,1]
	# print(intersect(nums1, nums2))
	# print(intersect1(nums1, nums2))
	print(intersect2(nums1, nums2))