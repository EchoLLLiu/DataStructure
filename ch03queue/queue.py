# coding = utf-8

__author__ = "LY"
__time__ = "2018/5/7"

class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		'''使用列表创建队列'''
		self.items = []

	def inQueue(self, data):
		'''入队列(头出尾进)'''
		self.items.append(data)

	def isEmpty(self):
		'''判断队列是否为空'''
		return self.items == []

	def deQueue(self):
		'''出队列'''
		if self.items == []:
			print("Queue is empty")
			return
		del self.items[0]

	def size(self):
		'''输出队列大小'''
		return len(self.items)

	def delete(self):
		'''销毁队列'''
		k = len(self.items)
		i = 0
		while k > 0:
			del self.items[i]
			k -= 1
		del k
		del i
		print("Delete queue successfully!")

if '__main__' == __name__:
	q =	Queue()
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

		


