# coding=utf-8
class DLNode(object):
	''' This is the node of double linklist '''
	def __init__(self, data, pnext = None, prior = None):
		self.data = data
		self.pnext = pnext
		self.prior = prior

class DLinkList(object):
	''' This is a class of double linklist , there some operators about double linklist '''
	''' DLinkList 与 DLnode不是同一种类，DLinkList.head是头结点，以此往后链接节点'''
	''' 循环双链表代码见注释部分 '''
	def __init__(self):
		''' Init the linklist '''
		self.head = None
		self.length = 0

	def CreateDLinkListR(self, List):
		''' This fuction is to create double linklist from list_front to list_rear '''
		if len(List) == 0:
			self.head = None
			self.length = 0
			return 

		p = DLNode(List[0])
		head = p
		for x in List[1:]:
			node = DLNode(x)
			p.pnext = node
			node.prior = p
			p = node
			del node
		#p.pnext = head
		#head.prior = p
		del p
		self.head = head
		self.length = len(List)
		return 

	def isEmpty(self):
		''' Whether the double linklist is empty '''
		return self.length == 0

	def appendDLList(self, data):
		''' Add a node after the double linklist '''
		node = DLNode(data)
		p = self.head
		if p == None:
			#node.pnext = node
			#node.prior = node
			self.head = node
			self.length = 1
			del p
			return 

		#while p.pnext != self.head:
		while p.pnext!= None:
			p = p.pnext
		p.pnext = node
		node.prior = p
		#node.pnext = self.head
		#self.head.prior = node
		del p 
		self.length += 1
		return 

	def deleteDLList(self, index):
		''' Delete the node in index '''
		''' index begin with 0 '''
		if index >= self.length:
			print("index超过链表长度")
			return 
		p = self.head
		for i in range(1,index):
			p = p.pnext
		q = p.pnext
		p.pnext = q.pnext
		q.pnext.prior = p
		self.length -= 1
		del q
		del p
		return 

	def updateDLList(self, index, data):
		''' Update the node in index by data '''
		''' index begin with 0 '''
		if index >= self.length:
			print("index超过链表长度")
			return 
		p = self.head
		for i in range(1,index+1):
			p = p.pnext
		p.data = data
		del p
		return 

	def getItem(self, index):
		''' Find the node in index '''
		if index >= self.length:
			print("index超过链表长度")
			return 
		p = self.head
		for i in range(1,index+1):
			p = p.pnext
		print(p.data)
		del p
		return 

	def getIndex(self, data):
		''' Find the index of data '''
		p = self.head
		index = 0
		#while index < self.length: 
		while p!= None:
			if p.data == data:
				print(index)
				del p
				del index
				return 
			p = p.pnext
			index += 1 
		del p
		print("链表中不存在data为%d的节点" % data)
		return 

	def insertDLList(self, index, data):
		''' Insert a node in index '''
		if index > self.length:
			print("index超过链表长度")
			return 
		node = DLNode(data)
		p = self.head
		for i in range(1,index):
			p = p.pnext
		node.pnext = p.pnext
		p.pnext.prior = node
		p.pnext = node 
		node.prior = p
		self.length += 1
		del p
		return 

	def delete(self):
		''' Delete the linklist '''
		p = self.head
		q = p.pnext
		#while q != self.head:
		while q != None:
			del p
			p = q
			q = p.pnext
		del p
		del q
		self.head = None
		self.length = 0
		print("链表删除完毕")
		return 

	def printDLList(self):
		'''Print the linklist'''
		if self.length == 0:
			print("链表为空！")
			return
		p = self.head
		#while p.pnext != self.head:
		while p!= None:
			print(p.data, end = " ")
			p = p.pnext

		#print(p.data)
		print("")
		return 

if __name__ == '__main__':
	List = [2,4,3,6,7]
	ll = DLinkList()
	print("创建链表：", end = "")
	ll.CreateDLinkListR(List)
	ll.printDLList()
	print("链表是否为空：", end = "")
	print("是" if ll.isEmpty() else "否")
	print("增加节点(data=5)：", end = "")
	ll.appendDLList(5)
	ll.printDLList()
	print("删除第2个节点：", end = "")
	ll.deleteDLList(2)
	ll.printDLList()
	print("删除第10个节点：", end = "")
	ll.deleteDLList(10)
	print("更新第1个节点(data=9)：", end = "")
	ll.updateDLList(1,9)
	ll.printDLList()
	print("更新第5个节点(data=10)：", end = "")
	ll.updateDLList(5,10)
	print("查找第4个节点：", end = "")
	ll.getItem(4)
	print("查找第5个节点：", end = "")
	ll.getItem(5)
	print("查找data=2的节点,其index为：", end = "")
	ll.getIndex(2)
	print("查找data=12的节点：", end = "")
	ll.getIndex(12)
	print("在第1位插入节点11：", end = "")
	ll.insertDLList(1,11)
	ll.printDLList()
	print("在第7位插入节点11：", end = "")
	ll.insertDLList(7,11)
	print("删除链表：", end = "")
	ll.delete()