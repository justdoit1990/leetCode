#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午5:29
# @Author  : Yanheng Wei
# @Site    : Haizhi
# @File    : linked_sum1.py
# @Software: PyCharm

class Node(object):
	def __init__(self, value):
		self.value = value
		self.__next_ = None

	def get_value(self):
		return self.value

	def get_next(self):
		try:
			return self.__next
		except:
			return None

	def set_value(self, value):
		self.value = value

	def set_next(self, next_):
		self.__next = next_


class LinkedList(object):
	def __init__(self):
		self.__head = None
		self.__size = 0

	def is_empty(self):
		if self.__head is None:
			return True

	def get_size(self):
		return self.__size

	def append_node(self, value):

		node = Node(value)

		if self.is_empty():
			self.__head = node
			self.__size += 1
		else:
			current = self.__head
			while current.get_next():
				current = current.get_next()
			current.set_next(node)
			self.__size += 1

	def delete_node(self, key):

		if self.is_empty():
			raise Exception("the linked list is empty")
		else:
			current = self.__head
			if current.get_value() == key:
				self.__head = current.get_next()
				self.__size -= 1
			else:
				while current.get_next():
					if current.get_value() == key:
						current.set_next(current.get_next())
						self.__size -= 1

	def pop(self):
		if self.is_empty():
			# print 'the linked list is empty!'
			return None
		else:
			temp = self.__head
			self.__head = temp.get_next()
			self.__size -= 1
			return temp

	def get_head(self):
		if self.is_empty():
			return None
		else:
			return self.__head



class LinkedSum(object):
	def __init__(self, list1, list2):
		self.linked_list1 = list1
		self.linked_list2 = list2
	def sum_linked_list(self):
		try:
			if self.linked_list1.get_size() != self.linked_list2.get_size() or self.linked_list1.get_size() == 0 or self.linked_list2.get_size() == 0:
				raise Exception("linked list error")
		except Exception, e:
			print e
		sum_list = LinkedList()
		l1 = self.linked_list1.pop()
		l2 = self.linked_list2.pop()
		while(l1):
			sum_list.append_node(l1.get_value()+l2.get_value())
			l1 = self.linked_list1.pop()
			l2 = self.linked_list2.pop()

		sum_temp = sum_list.get_head()
		while sum_temp:
			if sum_temp.get_value() > 9:
				shiwei = sum_temp.get_value()/10
				gewei = sum_temp.get_value()%10
				sum_temp.set_value(gewei)
				if sum_temp.get_next() is None:
					sum_list.append(Node(shiwei))
				else:
					sum_temp.get_next().set_value(sum_temp.get_next().get_value()+shiwei)
				sum_temp = sum_temp.get_next()

		result = []
		ll = sum_list.pop()
		while (ll):
			result.append(ll.get_value())
			ll = sum_list.pop()

		return result

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		ls = LinkedSum(l1, l2)
		result = ls.sum_linked_list()
		return result



if __name__ == "__main__":

	a = [2, 4, 3]
	b = [5, 6, 4]
	ls = LinkedSum(a, b)
	tst = ls.sum_linked_list()

	# print 'size %d', tst.get_size()

	ll = tst.pop()
	while(ll):
		print ll.get_value()
		ll = tst.pop()





