"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 

 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 

 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 

 示例： 

 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
 
 Related Topics 链表 数学

"""

"""
加法肯定是从最低位到最高位进行相加，也就是这里的链表头到链表尾进行相加，所以需要遍历链表。
我们令 l1 和 l2 指向两个链表的头，用一个 tmp 值来存储同一位相加的结果，
以及一个新的链表来存储 tmp 的值

存储 tmp%10 的值
设置哨兵节点,返回整个链表
"""
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    temp = 0
    res = ListNode(0)
    cur = res
    while l1 or l2 or temp != 0:
        if l1:
            temp += l1.val
            l1 = l1.next
        if l2:
            temp += l2.val
            l2 = l2.next

        cur.next = ListNode(temp % 10)
        temp //= 10
        cur = cur.next
    return res.next