# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/25 15:27'
# 归并排序实现


def merge_sort(item):
    """
    归并排序
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(nlogn)
    稳定排序算法
    :return:
    """
    n = len(item)
    if n <= 1:
        return item
    mid = n // 2
    left = merge_sort(item[:mid])
    right = merge_sort(item[mid:])
    left_pointer, right_pointer = 0, 0
    result = list()
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(merge_sort(li))