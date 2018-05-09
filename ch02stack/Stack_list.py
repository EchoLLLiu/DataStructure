# coding = utf-8

__author__ = 'LY'
__time__ = '2018/5/7'

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		'''初始化栈为空列表'''
		self.items = []

	def isEmpty(self):
		'''判断栈是否为空'''
		return self.items == []

	def size(self):
		'''返回栈的大小'''
		return len(self.items)

	def pop(self):
		'''出栈'''
		if len(self.items) == 0:
			print("Stack is empty, you can not pop anything")
			return
		del self.items[len(self.items) - 1]
		return 

	def push(self, num):
		'''入栈'''
		self.items.append(num)
		return 

	def peek(self):
		'''返回栈顶元素'''
		if self.items == []:
			print("Stack is empty, no peek")
			return
		return self.items[len(self.items) - 1]

	def printStack(self):
		'''打印栈'''
		for k in self.items:
			print(k, end = " ")
		print("")

	def delete(self):
		'''销毁栈'''
		k = len(self.items)
		i = 0
		while k > 0:
			del self.items[0]
			k -= 1
		del k
		del i
		print("delete Stack successfully!")

if '__main__' == __name__ :
	List = [1,2,3,4,5,6]
	l = Stack()
	print("将List压入栈中：", end = " ")
	for i in List:
		l.push(i)
	l.printStack()
	print("栈是否为空：", end = " ")
	print("空" if l.isEmpty() == True else "非空")
	print("栈的大小为：%d" % l.size())
	print("出栈：", end = " ")
	l.pop()
	l.printStack()
	print("入栈(num=10)：", end = " ")
	l.push(10)
	l.printStack()
	print("栈顶元素为：%d" % l.peek())
	l.delete()




		