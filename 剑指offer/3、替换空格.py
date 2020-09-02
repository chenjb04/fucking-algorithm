"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

"""


"""
Python内置replace方法
"""
def replaceSpace(s: str) -> str:
	return s.replace(' ', '%20')


"""
字符串是不可变对象，可以新建一个空字符串
"""
def replaceSpace1(s: str) -> str:
	res = ""
	for i in s:
		if i == ' ':
			res += '%20'
		else:
			res += i
	return res
 


if __name__ == '__main__':
	s = "We are happy."
	print(replaceSpace(s))
	print(replaceSpace1(s))