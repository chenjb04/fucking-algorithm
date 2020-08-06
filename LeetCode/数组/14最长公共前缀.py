"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
from typing import List


"""
方法一：
	思路：找到最短字符串当做基准元素。依次将基准元素和后面的元素进行比较不断更新基准元素，直到基准元素和所有元素都满足最长公共前缀的条件
"""
def longestCommonPrefix(strs: List[str]) -> str:
	# 处理临界
	if len(strs) == 0:
		return ''
	# 最小串当做基准元素
	prefix = min(strs, key=lambda x: len(x))
	for i in range(len(strs)):
		for j in range(len(prefix)):
			if strs[i].find(prefix) != 0:
				prefix = prefix[:len(prefix) - 1]
				continue
	return prefix


"""
方法二： zip函数
	思路：zip函数将传入对象打包成元组 
	["flower","flow","flight"] 打包后的结果：[('f', 'f', 'f'),('l', 'l', 'l'),('o', 'o', 'i')，('w', 'w', 'g')]
	set()函数，用来建立无序不重复的元素集，如果打包好的列表里的元组set后的长度为1，则是每个字符串中公有的字母，算为一个前缀字母，遇到set后不为1的元组时，则已经有不同字母了，退出查找，返回已找到的前缀字符串。

"""
def longestCommonPrefix1(strs: List[str]) -> str:
	# 处理临界
	if len(strs) == 0:
		return ''
	prefix = ''
	for i in zip(*strs):
		if len(set(i)) == 1:
			prefix += i[0]
		else:
			return prefix
	return prefix


if __name__ == '__main__':
	strs = ["flower","flow","flight"]
	print(longestCommonPrefix(strs))
	print(longestCommonPrefix1(strs))