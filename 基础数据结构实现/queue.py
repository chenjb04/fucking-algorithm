# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 18:41'
# 队列实现


class Queue(object):
    def __init__(self):
        self.__list = list()

    def enqueue(self, data):
        """
        往队列中添加元素
        :param data:
        :return:
        """
        self.__list.append(data)

    def dequeue(self):
        """
        出队
        :return:
        """
        return self.__list.pop(0)

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        if len(self.__list) > 0:
            return False
        else:
            return True

    def size(self):
        """
        返回队列大小
        :return:
        """
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    print("当前队列是否为空", q.is_empty())
    print("当前栈大小：", q.size())

    q.enqueue(1)
    q.enqueue(96)
    q.enqueue(55)
    print("出队元素为：", q.dequeue())
    print("当前队列是否为空", q.is_empty())
    print("当前队列大小：", q.size())