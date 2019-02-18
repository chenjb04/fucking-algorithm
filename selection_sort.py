# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 19:47'


def selection_sort(item):
    """
    选择排序实现
    最优时间复杂度：O(n^2)
    最坏时间复杂度：O(n^2)
    不稳定排序算法
    :param item:
    :return:
    """
    n = len(item)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if item[min_index] > item[i]:
                min_index = i
        item[j], item[min_index] = item[min_index], item[j]
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(selection_sort(li))