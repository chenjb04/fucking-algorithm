# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/15 20:19'


class SeqList(object):
    """
    顺序表实现
    用list实现list有点荒谬。。。。。。。。。。。
    """
    def __init__(self, size=8):
        # 初始化顺序表最大长度为8
        self.size = size
        self.num = 0
        self.data = [None] * self.size

    def is_empty(self):
        """
        判断线性表是否为空
        :return: True or False
        """
        if self.num is 0:
            return True
        else:
            return False

    def is_full(self):
        """
        判断顺序表是否为满
        :return: True or False
        """
        if self.num is self.size:
            return True
        else:
            return False

    def __getitem__(self, index):
        """
        获取顺序表中的某一位置值
        :param index: 索引值
        :return:
        """
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        """
        修改顺序表中的某个值
        :param key: 索引值
        :param value: 要修改的值
        :return:
        """
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < self.size:
            self.data[key] = value
        else:
            raise IndexError

    def append_end(self, value):
        """
        在表尾插入元素
        :return:
        """
        if self.is_full():
            # TODO：扩建顺序表
            print("顺序表已满")
        else:
            self.data[self.num] = value
            self.num += 1

    def rand_insert(self, key, value):
        """
        保序随机插入元素
        :param key: 要插入的索引位置
        :param value: 要插入的元素
        :return:
        """
        if self.is_full():
            # TODO：扩建顺序表
            print("顺序表已满")
        if not isinstance(key, int):
            raise TypeError
        if key < 0 or key > self.num:
            raise IndexError
        for i in range(self.num, key, -1):
            self.data[i] = self.data[i-1]
        self.data[key] = value
        self.num += 1

    def rand_remove(self, key=-1):
        """
        保序随机删除某一位置元素
        :param key: 删除位置的索引
        :return:
        """
        if not isinstance(key, int):
            raise TypeError
        if key > self.num:
            raise IndexError
        if key == -1:
            self.num -= 1
        else:
            for i in range(key, self.num-1):
                self.data[i] = self.data[i+1]
            self.num -= 1

    def reverse(self):
        """
        顺序表翻转
        :return:
        """
        i, j = 0, self.num - 1
        while i < j:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i, j = i + 1, j - 1

    def clear(self):
        """
        清空顺序表
        :return:
        """
        self.__init__()


if __name__ == '__main__':
    seq_list = SeqList()
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    seq_list.append_end(99)
    seq_list.append_end(23)
    seq_list.append_end("haha")
    seq_list.append_end(12.6)
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    seq_list.rand_insert(2, "python")
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    print(seq_list.__getitem__(2))

    seq_list.__setitem__(1, 100)
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    seq_list.rand_remove(1)
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    seq_list.reverse()
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))

    seq_list.clear()
    print("当前顺序表大小为:%d 表中元素个数为:%d 表中元素为:%s" % (seq_list.size, seq_list.num, seq_list.data))









