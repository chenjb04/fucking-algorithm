# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/2/13 18:49'
import timeit


def t1():
    li = list()
    for i in range(10000):
        li += [i]


def t2():
    li = list()
    for i in range(10000):
        li.append(i)


def t3():
    li = list(range(10000))


def t4():
    li = [i for i in range(10000)]


def t5():
    li = list()
    for i in range(10000):
        li.extend([i])


if __name__ == '__main__':
    timer1 = timeit.Timer("t1()", "from __main__ import t1")
    print("+:", timer1.timeit(number=1000))

    timer2 = timeit.Timer("t2()", "from __main__ import t2")
    print("append:", timer2.timeit(number=1000))

    timer3 = timeit.Timer("t3()", "from __main__ import t3")
    print("range:", timer3.timeit(number=1000))

    timer4 = timeit.Timer("t4()", "from __main__ import t4")
    print("[for]:", timer4.timeit(number=1000))

    timer5 = timeit.Timer("t5()", "from __main__ import t5")
    print("extend:", timer5.timeit(number=1000))
