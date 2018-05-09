# coding = utf-8

__author__ = "LY"
__time__ = "2018/5/8"

class CycleQueue(object):
	"""docstring for CircleQueue"""
	def __init__(self, maxsize, front=0, rear=0):
		'''循环队列有空间大小限制'''
		self.maxsize = maxsize
		self.items = [None] * self.maxsize
		self.front = 0
		self.rear = 0

	def inQueue(self, data):
		'''入队列(头出尾进)'''
		if (self.rear+1)%self.maxsize == self.front:
			print("Cycle queue is full, you can not add anything！")
			return
		self.rear = (self.rear+1) % self.maxsize
		self.items[self.rear] = data

	def isEmpty(self):
		'''判断队列是否为空'''
		return self.front == self.rear

	def deQueue(self):
		'''出队列'''
		if self.front == self.rear:
			print("Cycle queue is empty!")
			return
		self.front = (self.front+1) % self.maxsize
		self.items[self.front] = None

	def size(self):
		'''输出队列大小'''
		return (self.rear-self.front+self.maxsize) % self.maxsize

	def delete(self):
		'''销毁循环队列'''
		k = self.maxsize
		i = 0
		while k > 0:
			del self.items[i]
			k -= 1
		del k
		del i
		print("Delete cycle queue successfully!")

if '__main__' == __name__:
	q =	CycleQueue(5)
	List = [1,2,3,4]
	for i in List:
		q.inQueue(i)
	print("队列为：", q.items)
	print("队列是否为空：", "空" if q.isEmpty()==True else "非空")
	print("队列大小为：", q.size())
	q.deQueue()
	print("出队列：", q.items)
	print("队列大小为：", q.size())
	q.delete()