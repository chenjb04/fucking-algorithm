# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 18:54'
# 双端队列实现


class Deque(object):
    """
    双端队列实现
    """
    def __init__(self):
        self.__list = list()

    def add_front(self, data):
        """
        往队列头部添加元素
        :param data:
        :return:
        """
        self.__list.insert(0, data)

    def add_end(self, data):
        """
        队列尾部添加元素
        :param data:
        :return:
        """
        self.__list.append(data)

    def pop_front(self):
        """
        从头部出队
        :return:
        """
        return self.__list.pop(0)

    def pop_end(self):
        """
        尾部出队
        :return:
        """
        return self.__list.pop()

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
    q = Deque()
    print("当前队列是否为空", q.is_empty())
    print("当前栈大小：", q.size())

    q.add_front(1)
    q.add_front(96)
    q.add_end(55)
    print("出队元素为：", q.pop_front())
    print("出队元素为：", q.pop_end())
    print("当前队列是否为空", q.is_empty())
    print("当前队列大小：", q.size())