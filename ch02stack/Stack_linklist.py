# coding = utf-8

__author__ = 'LY'
__time__ = '2018/5/7'

class SNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = None

class Stack(object):
	"""docstring for Stack"""
	def __init__(self, length=0, head=None):
		self.length = length
		self.head = None

	def isEmpty(self):
		'''判断栈是否为空'''
		return self.head == None

	def size(self):
		'''返回栈的大小'''
		if self.head == None:
			return 0
		p = self.head
		count = 0
		while p != None :
			count += 1
			p = p.next
		del p
		return count

	def pop(self):
		'''出栈'''
		if self.head == None:
			print("Stack is empty, you can not pop anything")
			return 
		p = self.head
		q = p.next
		while q.next != None:
			p = p.next
			q = p.next
		p.next = q.next
		self.length -= 1
		del p
		del q
		return 

	def push(self, num):
		'''入栈'''
		node = SNode(num)
		if self.head == None:
			self.head = node
			return
		p = self.head
		while p.next != None:
			p = p.next
		p.next = node
		del p
		return 

	def peek(self):
		'''返回栈顶元素'''
		if self.head == None:
			print("Stack is empty, no peek")
			return
		p = self.head
		while p.next != None:
			p = p.next
		return p.val

	def printStack(self):
		'''打印栈'''
		if self.head == None:
			print("Stack is empty")
			return 
		p = self.head
		while p != None:
			print(p.val, end = " ")
			p = p.next
		print("")
		del p
		return 

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