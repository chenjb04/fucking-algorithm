# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/21 17:22'
# 希尔排序实现


def shell_sort(item):
    """
    希尔排序
    最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n^2)
    不稳定排序算法
    :param item:
    :return:
    """
    n = len(item)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if item[i] < item[i-gap]:
                    item[i], item[i - gap] = item[i - gap], item[i]
                    i -= gap
                else:
                    break
        gap //= 2

    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(shell_sort(li))

