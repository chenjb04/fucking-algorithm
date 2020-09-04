# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/18 13:52'
# 双向链表实现


class Node(object):
    """
    双向链表节点实现
    """
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkList(object):
    """
    双向链表实现
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """
        判断双向链表是否为空
        :return:
        """
        return self.__head is None

    def length(self):
        """
        双向链表长度
        """
        # cur用来移动遍历节点
        cur = self.__head
        # count为计数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历双向链表
        :return:
        """
        cur = self.__head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

    def add(self, data):
        """
        头插法
        :param data: 插入的数据
        :return:
        """
        node = Node(data)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, data):
        """
        尾部添加节点 尾插法
        :param data: 插入的数据
        :return:
        """
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            count = 0
            cur = self.__head
            while count < index:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, data):
        """
        删除节点
        :param data:
        :return:
        """
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                # 判断是否删除的节点为头结点
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表是否只有一个节点
                    if cur.next:
                        cur.next.prev = None
                    return True
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    return True
            else:
                cur = cur.next
        return False

    def search(self, data):
        """
        判断节点是否存在
        :param data: 要查找的数据
        :return:
        """
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    double_link_list = DoubleLinkList()
    print("当前链表是否为空：", double_link_list.is_empty())
    print("当前链表长度为：", double_link_list.length())

    double_link_list.append(99)
    print("当前链表是否为空：", double_link_list.is_empty())
    print("当前链表长度为：", double_link_list.length())

    double_link_list.append(23)
    double_link_list.append(89)
    double_link_list.append("python")
    double_link_list.append(12.66)
    double_link_list.add(27)
    double_link_list.insert(4, 0)
    double_link_list.remove(27)
    double_link_list.travel()

    print(double_link_list.search(23))
