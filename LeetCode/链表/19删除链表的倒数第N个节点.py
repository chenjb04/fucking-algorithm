"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
1、定义一个哨兵节点，指向头结点
2、定义两个快慢指针，指向头结点
3、让快指针先走n步
4、快慢指针一起走，直到快指针走完
5、慢指针的next指向慢指针的next 的next，实现删除操作
6、返回头结点
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 哨兵节点
        result = ListNode(0)
        # 哨兵节点的next节点指向头节点
        result.next = head
        # slow慢指针， 指向头节点
        slow = result
        # fast快指针指向头节点
        fast = result
        # 先让快指针走n步
        for _ in range(n):
            fast = fast.next
        # 快慢指针一起走，直到快指针走到头
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        # 实现删除
        slow.next = slow.next.next
        return result.next