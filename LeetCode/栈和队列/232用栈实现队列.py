# 使用栈实现队列的下列操作： 
# 
#  
#  push(x) -- 将一个元素放入队列的尾部。 
#  pop() -- 从队列首部移除元素。 
#  peek() -- 返回队列首部的元素。 
#  empty() -- 返回队列是否为空。 
#  
# 
#  
# 
#  示例: 
# 
#  MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false 
# 
#  
# 
#  说明: 
# 
#  
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#  
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。 
#  
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
# from collections import deque
#
#
# class Stack:
#     def __init__(self):
#         self.items = deque()
#
#     def push(self, val):
#         return self.items.append(val)
#
#     def pop(self):
#         return self.items.pop()
#
#     def empty(self):
#         return len(self.items) == 0
#
#     def top(self):
#         return self.items[-1]


"""
解题思路：
	用两个栈实现队列，一个栈作为压入数据使用，一个栈作为弹出数据使用。

	push操作:
		直接往stack1 push数据

	pop操作:
		 把stack1中的数据全部pop出去 push到stack2中，那么顺序就像队列一样了
		 注意：如果stack2中不为空，stack1中的数据是不能push到stack2中的，如果push了，会出现顺序问题
	
	peek操作:
		返回stack2中的栈顶元素

	empty操作:
		stack1和stack2不为空 则返回Fasle 反之 返回True

"""
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        :return:
        """
        return len(self.stack2) == 0 and len(self.stack1) == 0



