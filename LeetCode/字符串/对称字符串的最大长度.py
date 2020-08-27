"""
求一个字符串中对称字符串的最大长度 
输入：google
输出：4
解释：goog为最大对称字符串，长度为4

"""

"""
1.将首尾两个字符相同的串切片
2.将字符反转，判断是否对称字符串
3.求对称字符串长度存入列表
4.输出列表中的最大值
"""
def max_length(string):
	n = len(string)
	temp = []
	for i in range(n - 1):
		for j in range(i+1, n):
			if string[i] == string[j]:
				str_small = string[i:j + 1]
				temp.append(str_small)
	res = []
	for i in temp:
		if i == i[::-1]:
			res.append(len(i))
	return max(res)

 

if __name__ == '__main__':
	string = "google"
	print(max_length(string))
	string = "mam"
	print(max_length(string))
	string = "hello"
	print(max_length(string))
