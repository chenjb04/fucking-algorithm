"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
from typing import List


# 方法一：反向遍历
def removeElement(nums: List[int], val: int) -> int:
	for i in range(len(nums) - 1, -1, -1):
		if nums[i] == val:
			nums.pop(i)
	return len(nums)


# 双指针法
"""
初始化快慢指针，快指针遍历数组，如果快指针指向元素等于val，则快指针往后移一格，否则将快指针元素复制到慢指针位置，快慢指针各往后移一格

最后返回慢指针的位置
"""
def removeElement1(nums: List[int], val: int) -> int:
	if not nums:
		return 0
	fast, slow = 0, 0
	while fast < len(nums):
		if nums[fast] == val:
			fast += 1
		else:
			nums[slow] = nums[fast]
			fast += 1
			slow += 1
	return slow

if __name__ == '__main__':
	nums = [0,1,2,2,3,0,4,2]
	print(removeElement(nums, 2))
	print(removeElement1(nums, 2))