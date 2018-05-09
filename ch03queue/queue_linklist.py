# coding = utf-8

__author__ = "LY"
__time__ = "2018/5/7"

class QNode(object):
	"""docstring for QNode"""
	def __init__(self, val, next=None):
		self.val = val
		self.next = None
		
class Queue(object):
	"""docstring for Queue"""
	def __init__(self, front=None, rear=None):
		'''使用链表创建队列,front指头，rear指尾的后一个'''
		self.front = front
		self.rear = rear

	def inQueue(self, data):
		'''入队列(头出尾进)'''
		node = QNode(data)
		if self.front == None:
			self.front = node
			self.rear = node.next
			return
		p = self.front
		while p.next != None:
			p = p.next
		p.next = node
		self.rear = node.next
		del p
		return

	def isEmpty(self):
		'''判断队列是否为空'''
		return self.front == None

	def deQueue(self):
		'''出队列'''
		if self.front == None:
			print("Queue is empty")
			return
		tmp = self.front
		self.front = tmp.next
		del tmp

	def size(self):
		'''输出队列大小'''
		p = self.front
		lens = 0
		while p != None:
			lens += 1
			p = p.next
		del p
		return lens

	def printQue(self):
		'''打印队列'''
		p = self.front
		while  p != None:
			print(p.val, end = " ")
			p = p.next
		print("")

	def delete(self):
		'''销毁队列'''
		p = self.front
		q = p.next
		while q != None:
			del p
			p = q
			q = p.next
		del p
		del q
		self.front = None
		self.rear = None
		print("Delete queue successfully!")


if '__main__' == __name__:
	q =	Queue()
	List = [1,2,3,4]
	for i in List:
		q.inQueue(i)
	print("队列为：", end = " ")
	q.printQue()
	print("队列是否为空：", "空" if q.isEmpty()==True else "非空")
	print("队列大小为：", q.size())
	print("出队列：", end = " ")
	q.deQueue()
	q.printQue()
	print("队列大小为：", q.size())
	q.delete()
		