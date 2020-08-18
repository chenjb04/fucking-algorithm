"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""
from typing import List


"""
直接循环 如果末尾不是9，直接给末尾数字加一返回
如果末尾是9，末尾置为0，下一轮循环，虑特殊情况：99
此时需要检查最后一次for循环的数字是不是0
即digits[0]是否为0，如果是0，则遇到了特殊情况
此时需要在数组最前面加一个数字1，然后返回即可
"""
def plusOne(digits: List[int]) -> List[int]:
	for i in range(len(digits)-1, -1, -1):
		if digits[i] != 9:
			digits[i] += 1
			return digits
		else:
			digits[i] = 0
			if digits[0] == 0:
				digits.insert(0, 1)
				return digits

"""
转换为数字 +1之后在转换为list
"""
def plusOne1(digits: List[int]) -> List[int]:
	a = [i *10**index for index,i in enumerate(digits[::-1])]
	num = sum(a) + 1
	return [int(x) for x in str(num)]


if __name__ == '__main__':
	digits = [9, 9]
	# print(plusOne(digits))
	print(plusOne1(digits))