"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
利用栈来实现
"""
def reversePrint(head: ListNode) -> List[int]:
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur.val)
        cur = cur.next
    return [stack.pop() for _ in range(len(stack))]