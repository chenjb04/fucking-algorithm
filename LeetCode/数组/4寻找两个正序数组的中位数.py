"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 

 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 

 你可以假设 nums1 和 nums2 不会同时为空。 

 

 示例 1: 

 nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
 

 示例 2: 

 nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
 
 Related Topics 数组 二分查找 分治算法

"""
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
	# 交换顺序 第一个数组总小于第二个数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    len1, len2 = len(nums1), len(nums2)
    # 第一个数组的左边界 右边界 合并数组的中间点
    left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
    # 第一个序列的中间点
    mid1 = (left + right) // 2
    # 第二个数组的中间点
    mid2 = half_len - mid1

    while left < right:
        if mid1 < len1 and nums2[mid2 - 1] > nums1[mid1]:
            left = mid1 + 1
        else:
            right = mid1
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

    if mid1 == 0:
        max_of_left = nums2[mid2 - 1]
    elif mid2 == 0:
        max_of_left = nums1[mid1 - 1]
    else:
        max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

    if (len1 + len2) % 2 == 1:
        return max_of_left

    if mid1 == len1:
        min_of_right = nums2[mid2]
    elif mid2 == len2:
        min_of_right = nums1[mid1]
    else:
        min_of_right = min(nums1[mid1], nums2[mid2])

    return (max_of_left + min_of_right) / 2


if __name__ == '__main__':
	nums1 = [1, 2]
	nums2 = [3, 4]
	print(findMedianSortedArrays(nums1, nums2))
	nums1 = [1, 3]
	nums2 = [2]
	print(findMedianSortedArrays(nums1, nums2))

