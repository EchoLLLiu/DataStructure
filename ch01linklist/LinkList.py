# coding=utf-8
class LNode(object):
	''' This is the node of linklist '''
	def __init__(self, data, pnext = None):
		self.data = data
		self.pnext = pnext

class LinkList(object):
	''' This is a class of linklist , there some operators about linklist '''
	''' LinkList 与 Lnode不是同一种类，LinkList.head是头结点，以此往后链接节点'''
	''' 循环单链表代码见注释部分 '''
	def __init__(self):
		''' Init the linklist '''
		self.head = None
		self.length = 0

	def CreateLinkListR(self, List):
		''' This fuction is to create linklist from list_front to list_rear '''
		if len(List) == 0:
			self.head = None
			self.length = 0
			return 

		p = LNode(List[0])
		head = p
		for x in List[1:]:
			node = LNode(x)
			p.pnext = node
			p = node
			del node
		#p.pnext = head
		del p
		self.head = head
		self.length = len(List)
		return 

	def isEmpty(self):
		''' Whether the linklist is empty '''
		return self.length == 0

	def appendLList(self, data):
		''' Add a node after the linklist '''
		node = LNode(data)
		p = self.head
		if p == None:
			#node.pnext = node
			self.head = node
			self.length = 1
			del p
			return 

		#while p.pnext != self.head:
		while p.pnext!= None:
			p = p.pnext
		p.pnext = node
		#node.pnext = self.head
		del p 
		self.length += 1
		return 

	def deleteLList(self, index):
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
		self.length -= 1
		del q
		del p
		return 

	def updateLList(self, index, data):
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
				del p
				print(index)
				del index
				return 
			p = p.pnext
			index += 1 
		del p
		print("链表中不存在data为%d的节点" % data)
		return 

	def insertLList(self, index, data):
		''' Insert a node in index '''
		if index > self.length:
			print("index超过链表长度")
			return 
		node = LNode(data)
		p = self.head
		for i in range(1,index):
			p = p.pnext
		node.pnext = p.pnext
		p.pnext = node
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

	def printLList(self):
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
	ll = LinkList()
	print("创建链表：", end = "")
	ll.CreateLinkListR(List)
	ll.printLList()
	print("链表是否为空：", end = "")
	print("是" if ll.isEmpty() else "否")
	print("增加节点(data=5)：", end = "")
	ll.appendLList(5)
	ll.printLList()
	print("删除第2个节点：", end = "")
	ll.deleteLList(2)
	ll.printLList()
	print("删除第10个节点：", end = "")
	ll.deleteLList(10)
	print("更新第1个节点(data=9)：", end = "")
	ll.updateLList(1,9)
	ll.printLList()
	print("更新第5个节点(data=10)：", end = "")
	ll.updateLList(5,10)
	print("查找第4个节点：", end = "")
	ll.getItem(4)
	print("查找第5个节点：", end = "")
	ll.getItem(5)
	print("查找data=2的节点,其index为：", end = "")
	ll.getIndex(2)
	print("查找data=12的节点：", end = "")
	ll.getIndex(12)
	print("在第1位插入节点11：", end = "")
	ll.insertLList(1,11)
	ll.printLList()
	print("在第7位插入节点11：", end = "")
	ll.insertLList(7,11)
	print("删除链表：", end = "")
	ll.delete()