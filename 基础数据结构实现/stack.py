# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 18:12'
# list实现栈


class Stack(object):
    """
    list实现栈
    """

    def __init__(self):
        self.__list = list()

    def push(self, data):
        """
        添加新的元素到栈顶
        :param data: 数据
        :return:
        """
        self.__list.append(data)

    def pop(self):
        """
        弹出栈顶元素
        :return:
        """
        return self.__list.pop()

    def peek(self):
        """
        返回栈顶元素
        :return:
        """
        if self.is_empty():
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        """
        判断栈是否为空
        :return:
        """
        if len(self.__list) > 0:
            return False
        else:
            return True

    def size(self):
        """
        返回栈中元素数量
        :return:
        """
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    print("当前栈是否为空", s.is_empty())
    print("当前栈大小：", s.size())

    s.push(1)
    s.push(96)
    s.push(55)
    print("当前栈顶元素为：", s.peek())
    print("出栈元素为：", s.pop())
    print("当前栈顶元素为：", s.peek())
    print("当前栈是否为空", s.is_empty())
    print("当前栈大小：", s.size())