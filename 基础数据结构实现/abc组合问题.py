# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/9 12:17'
# 如果 a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有的a,b,c可能的组合


# 效率低下算法 时间复杂度为 O(n^3)
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if (a + b + c == 1000) and (a**2+b**2 == c**2):
#                 print("a,b,c=", a, b, c)


# 改进算法 时间复杂度为 O(n^2)
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print('a,b,c=', a, b, c)


# 时间复杂度计算规则
"""
1.基本操作：只有常数项，O(1)
2.顺序结构：按加法计算
3.循环结构：按乘法计算
4.分支结构：取最大值
5.只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
时间复杂度大小关系：
O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)
"""
