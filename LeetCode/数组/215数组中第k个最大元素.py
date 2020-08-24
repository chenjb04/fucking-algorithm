"""
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  示例 1: 
# 
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  说明: 
# 
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#  Related Topics 堆 分治算法

"""
from typing import List	


def findKthLargest(nums: List[int], k: int) -> int:
	nums.sort(reverse=True)
	return nums[k - 1]


"""
构建最小堆
"""
def findKthLargest1(nums: List[int], k: int) -> int:
    import heapq
    heap = []
    heapq.heapify(heap)
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == '__main__':
	nums = [3,2,3,1,2,4,5,5,6]
	k = 4
	print(findKthLargest(nums, k))
	print(findKthLargest1(nums, k))
