# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/19 19:01'
# 插入排序


def insert_sort(item):
    """
    插入排序实现
    最优时间复杂度：O(n)
    最坏时间复杂度：O(n^2)
    稳定排序算法
    :param item:
    :return:
    """
    n = len(item)
    for j in range(1, n):
        i = j
        while i > 0:
            if item[i] < item[i-1]:
                item[i], item[i-1] = item[i-1], item[i]
                i -= 1
            else:
                break
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(insert_sort(li))













