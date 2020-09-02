"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

"""
from typing import List


"""
暴力破解
"""
def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
	for i in matrix:
		for j in i:
			if target == j:
				return True
	return False


"""
从左下角开始搜索，当该值小于 target 值时，向右搜索；大于 target 值时，向上搜索。如果找到 target 则返回 True，否则返回 False。
"""
def findNumberIn2DArray1(matrix: List[List[int]], target: int) -> bool:
	if not matrix:
		return False
	# 行长度
	row_len = len(matrix)
	# 列长度
	col_len = len(matrix[0])
	row = row_len - 1
	col = 0
	while row >=0 and col < col_len:
		if matrix[row][col] == target:
			return True
		elif matrix[row][col] > target:
			row -= 1
		elif matrix[row][col] < target:
			col += 1
		else:
			return False
	return False


if __name__ == '__main__':
	matrix = [
			  [1,   4,  7, 11, 15],
			  [2,   5,  8, 12, 19],
			  [3,   6,  9, 16, 22],
			  [10, 13, 14, 17, 24],
			  [18, 21, 23, 26, 30]
			]
	target = 5
	print(findNumberIn2DArray(matrix, target))
	target = 20
	print(findNumberIn2DArray(matrix, target))

	target = 5
	print(findNumberIn2DArray1(matrix, target))
	target = 20
	print(findNumberIn2DArray1(matrix, target))
	