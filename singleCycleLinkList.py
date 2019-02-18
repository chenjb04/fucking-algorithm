# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 14:27'
# 单向循环链表实现


class Node(object):
    """
    单向循环链表节点
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleCycleLinkList(object):
    """
    单向循环链表实现
    """
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head is None

    def length(self):
        """
        链表长度
        """
        if self.is_empty():
            return 0
        # cur用来移动遍历节点
        cur = self.__head
        # count为计数
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.data, end=" ")
                cur = cur.next
            # cur指向尾节点
            print(cur.data)
            print("")

    def add(self, data):
        """
        头插法
        :param data: 插入的数据
        :return:
        """
        node = Node(data)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, data):
        """
        尾部添加节点 尾插法
        :param data: 插入的数据
        :return:
        """
        node = Node(data)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def insert(self, index, data):
        """
        指定位置添加节点
        :param index: 位置从0开始
        :param data: 插入的数据
        :return:
        """
        if index <= 0:
            self.add(data)
        elif index > (self.length() - 1):
            self.append(data)
        else:
            node = Node(data)
            pre = self.__head
            count = 0
            while count < (index - 1):
                pre = pre.next
                count += 1
            # 循环结束 pre指向index-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, data):
        """
        删除节点
        :param data:
        :return:
        """
        if self.is_empty():
            return False
        else:
            cur = self.__head
            pre = None
            while cur.next != self.__head:
                if cur.data == data:
                    # 判断是否删除的节点为头结点
                    if cur == self.__head:
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                        return True
                    else:
                        pre.next = cur.next
                        return True
                else:
                    pre = cur
                    cur = cur.next
            if cur.data == data:
                if cur == self.__head:
                    # 只有一个节点
                    self.__head = None
                    return True
                else:
                    pre.next = cur.next
                    return True
            return False

    def search(self, data):
        """
        判断节点是否存在
        :param data: 要查找的数据
        :return:
        """
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next != self.__head:
                if cur.data == data:
                    return True
                else:
                    cur = cur.next
            if cur.data == data:
                return True
            return False


if __name__ == '__main__':
    link_node = Node(100)
    single_cycle_link_list = SingleCycleLinkList()
    print("当前链表是否为空：", single_cycle_link_list.is_empty())
    print("当前链表长度为：", single_cycle_link_list.length())

    single_cycle_link_list.append(99)
    print("当前链表是否为空：", single_cycle_link_list.is_empty())
    print("当前链表长度为：", single_cycle_link_list.length())

    single_cycle_link_list.append(23)
    single_cycle_link_list.append(89)
    single_cycle_link_list.append("python")
    single_cycle_link_list.append(12.66)
    single_cycle_link_list.add(27)
    single_cycle_link_list.insert(4, 0)
    single_cycle_link_list.remove(27)
    single_cycle_link_list.travel()

    print(single_cycle_link_list.search(23))