# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  
#  push(x) —— 将元素 x 推入栈中。 
#  pop() —— 删除栈顶的元素。 
#  top() —— 获取栈顶元素。 
#  getMin() —— 检索栈中的最小元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  pop、top 和 getMin 操作总是在 非空栈 上调用。 
#  
#  Related Topics 栈 设计


"""
解题思路：
    使用两个栈，一个栈(stack)和普通的栈一样，一个栈为最小栈(min_stack)，用来存放最小元素的栈，保证栈顶一定是最小元素，
    那么只需要返回最小栈的栈顶元素，即为题解。

    push操作：
        stack栈正常push数据x，判断min_stack栈是否为空
        min_stack栈为空，把x也push到min_stack栈
        min_stack栈不为空且x小于等于min_stack栈顶元素，则x push到min_stack栈
        min_stack栈不为空且x大于min_stack栈顶元素，则x 不用push到min_stack栈

    pop操作：
        stack栈正常pop, 如果stack栈pop的值和min_stack栈栈顶元素相等，则min_stack栈也pop

    top操作:
        直接返回stack栈顶元素

    getmin操作:
        返回min_stack栈顶元素即为最小元素

"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
