"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。 

给出两个整数 x 和 y，计算它们之间的汉明距离。 

注意： 
0 ≤ x, y < 231. 

示例: 


输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
		↑  ↑

上面的箭头指出了对应二进制位不同的位置。

"""


"""
python 内置函数
"""
def hammingDistance(x: int, y: int) -> int:
	return bin(x ^ y).count('1')


"""
先异或 向右移位，检查最后一位是否1
"""
def hammingDistance1(x: int, y: int) -> int:
	xor = x ^ y
	count = 0
	while xor:
		if xor & 1:
			count += 1
		xor = xor >> 1
	return count



if __name__ == '__main__':
	x = 1
	y = 4
	print(hammingDistance(x, y))
	print(hammingDistance1(x, y))