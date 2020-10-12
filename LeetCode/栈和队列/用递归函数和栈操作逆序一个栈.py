"""

一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈转置后，
从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，
但是只能用递归函数来实现，不能用其他的数据结构。
"""

"""
解题思路:
	需要两个递归函数，get_remove_last将栈底元素返回并移除； reverse栈的逆序

	get_remove_last:
		先pop出栈顶元素
		然后弹出并返回少了一个元素的栈的栈底元素
		最后把value压入栈顶
	reverse:
		调用get_remove_last获取栈底元素
		然后调用reverse对少了一个元素的栈进行逆序处理
		最后把value压入栈， 就实现了栈元素的逆序
"""
class ReverseStack:
	def __init__(self, stack):
		self.stack = stack

	def get_remove_last(self):
		"""栈顶元素返回并移除"""
		value = self.stack.pop()
		if self.stack.empty():
			return value
		res = self.get_remove_last()
		self.stack.push(value)
		return res

	def reverse(self):
		if self.stack.empty():
			return
		value = self.get_remove_last()
		self.reverse()
		self.stack.push(value)


if __name__ == '__main__':
	class Stack:
		def __init__(self):
			self.stack = []

		def push(self,x):
			self.stack.append(x)

		def pop(self):
			return self.stack.pop()

		def empty(self):
			if len(self.stack) == 0:
				return True
			return False

		def traverse(self):
			while self.stack: 
				print(self.pop(), end=' ')

			print()

	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	# stack.traverse()

	reverse_stack = ReverseStack(stack)
	reverse_stack.reverse()
	stack.traverse()