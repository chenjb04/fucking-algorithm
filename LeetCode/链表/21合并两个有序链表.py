"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

 示例： 

 输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
 
 Related Topics 链表
"""

"""
1、设置一个哨兵节点，它的next指向l1或者l2中其中较小一个，直到l1或者l2指向None
2、这样到了最后，如果l1还是l2中任意一方还有余下元素没有用到，那余下的这些元素一定大于已经合并完的链表（因为是有序链表）
3、需要将这些元素全部追加到合并完的链表后
"""
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 设置一个哨兵节点
    result = ListNode(0)
    cur = result
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 is not None:
        cur.next = l1
    if l2 is not None:
        cur.next = l2
    return result.next