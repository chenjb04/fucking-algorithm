# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 19:11'


def bubble_sort(item):
    """
    冒泡排序实现
    最优时间复杂度：O(n)
    最坏时间复杂度：O(n^2)
    稳定排序算法
    :param item: 排序的元素
    :return:
    """
    # j代表遍历趟数
    for j in range(0, len(item)):
        # count 表示交换的次数
        count = 0
        # 从头到尾一趟遍历结果
        for i in range(0, len(item)-1-j):
            if item[i] > item[i+1]:
                item[i], item[i+1] = item[i+1], item[i]
                count += 1
        # 最优情况
        if count == 0:
            return item
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(bubble_sort(li))
