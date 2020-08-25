"""
给定一个链表，判断链表中是否有环。 

 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 

 

 示例 1： 

 输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
 

 

 示例 2： 

 输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
 

 

 示例 3： 

 输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

 进阶： 

 你能用 O(1)（即，常量）内存解决此问题吗？ 
 Related Topics 链表 双指针

"""


"""
快慢指针，快指针每次走两步，慢指针走一步
当快慢指针相遇，说明存在环
"""
def hasCycle(head: ListNode) -> bool:
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        if slow == fast:
            return True
        fast = fast.next.next
        slow = slow.next
    return False
