"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


"""

"""
python 内置方法find
"""
def strStr(haystack: str, needle: str) -> int:
	if not needle:
		return 0
	if not haystack:
		return -1
	return haystack.find(needle)


def strStr1(haystack: str, needle: str) -> int:
	if not needle:
		return 0
	if not haystack:
		return -1
	n = len(haystack)
	m = len(needle)
	i = 0
	while i < n - m:
		if haystack[i:i+m] == needle:
			return i
		else:
			i += 1
	if i > m -n :
		return -1


if __name__ == '__main__':
	haystack = "hello"
	needle = "ll"
	print(strStr(haystack, needle))
	print(strStr1(haystack, needle))
	haystack = "aaaaa"
	needle = "bba"
	print(strStr(haystack, needle))
	print(strStr1(haystack, needle))