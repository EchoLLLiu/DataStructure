# coding=utf-8
import time
class Node(object):
	"""docstring for Node"""
	def __init__(self, val, pnext=None):
		self.val = val
		self.pnext = pnext

class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self, head=None, length=0):
		self.head = head
		self.length = length

	def createLList(self, List):
		'''创建链表'''
		lens = len(List)
		if lens == 0:
			self.head = None
			self.length = 0
			return 
		node = Node(List[0])
		head = node
		p = head
		for i in range(1,lens):
			node = Node(List[i])
			p.pnext = node
			p = p.pnext
			del node
		del p
		self.head = head
		self.length = lens
		del head
		return self.head

	def printLList(self):
		'''打印链表'''
		p = self.head
		if p==None:
			print("None")
			return
		while p!=None:
			print(p.val, end=" ")
			p = p.pnext
		print("")
		return

class Solution(object):
	"""docstring for Solution"""
	def merge(self, LList1, LList2):
		'''合并链表，按照从小到大顺序'''
		if LList1.length == 0:
			return LList2
		if LList2.length == 0:
			return LList1
		p = LList1.head
		q = LList2.head
		MLList = LinkList()
		if p.val < q.val:
			MLList.head = p
			p = p.pnext
		else:
			MLList.head = q
			q = q.pnext
		tmp = MLList.head
		while p!=None and q!=None:
			if p.val < q.val:
				tmp.pnext = p
				p = p.pnext
			else:
				tmp.pnext = q
				q = q.pnext
			tmp = tmp.pnext
		# 链表1还未结束，链表2结束
		if p != None:
			tmp.pnext = p
		# 链表2还未结束，链表1结束
		if q != None:
			tmp.pnext = q
		del tmp
		del p
		del q
		return MLList

if '__main__' == __name__:
	List1 = [11,13,15,17,19]
	List2 = [2,4,6,7,10]
	LList1 = LinkList()
	LList1.createLList(List1)
	LList1.printLList()
	LList2 = LinkList()
	LList2.createLList(List2)
	LList2.printLList()
	s = Solution()
	temp = s.merge(LList1, LList2)
	temp.printLList()



