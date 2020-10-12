"""
一个栈中的元素为整型， 现在想从栈顶到栈底按从大到小的顺序排序，只允许申请一个栈
"""


"""
解题思路：
	要排序的栈为stack栈，辅助栈为help,在stack执行pop操作,弹出的元素记为cur

	如果cur小于或者等于help栈顶元素，把cur压入help栈

	如果cur大于help栈顶元素，则把help元素弹出，压入stack栈中，
	直到cur小于或者等于help栈顶元素，把cur压入help栈

	最后把help栈中元素压入到stack栈中

"""
class SortedStack:

    def __init__(self):
    	self.stack = []
    	self.help = []

    def push(self, x):
    	self.stack.append(x)

    def sort_stack(self):
    	while self.stack:
    		cur = self.stack.pop()
	    	while len(self.help) != 0 and cur < self.help[-1]:
	    		self.stack.append(self.help.pop())
	    	self.help.append(cur)
    	while len(self.help) != 0:
    		self.stack.append(self.help.pop())

    def traverse(self):
    	print(self.stack)


if __name__ == '__main__':
	sort_stack = SortedStack()
	sort_stack.push(2)
	sort_stack.push(4)
	sort_stack.push(1)
	sort_stack.push(5)
	sort_stack.push(3)
	sort_stack.sort_stack()
	sort_stack.traverse()
