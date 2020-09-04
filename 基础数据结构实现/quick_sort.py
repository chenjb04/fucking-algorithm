# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/21 19:26'
# 快速排序实现


def quick_sort(item, first, last):
    """
    快速排序
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n^2)
    不稳定排序算法
    :param item:
    :param first:起始值索引
    :param last:最后值索引
    :return:
    """
    if first < last:
        mid_value = item[first]
        low = first
        high = last
        while low < high:
            while (low < high) and item[high] >= mid_value:
                high -= 1
            item[low] = item[high]

            while (low < high) and item[low] < mid_value:
                low += 1
            item[high] = item[low]
        item[low] = mid_value
        quick_sort(item, first, low-1)
        quick_sort(item, low+1, last)
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(quick_sort(li, 0, len(li)-1))

