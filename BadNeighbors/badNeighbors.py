#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 下午12:46
# @Author  : Yanheng Wei
# @File    : badNeighbors.py
# @Software: PyCharm


class BadNeighbors(object):
	'''
	注意特殊状态，列表末尾
	'''

	def __init__(self, input_list):
		self.input_list = input_list

	def sub_max_donation(self, input_ls):
		# 不考虑列表末尾情况下的求取最大不连续和
		include_current = [0]*len(input_ls)
		non_include = [0]*len(input_ls)
		include_current[0] = input_ls[0]
		non_include[0] = 0
		max_donation_value = input_ls[0]
		include_top = True
		for i in range(1, len(input_ls)):
			include_current[i] = non_include[i-1] + input_ls[i]
			non_include[i] = max_donation_value
			if include_current[i] > non_include[i]:
				include_top = not include_top
				max_donation_value = include_current[i]
			else:
				max_donation_value = non_include[i]
		return max_donation_value

	def max_donation(self):
		input_list_top = self.input_list[1:]
		input_list_bottom = self.input_list[:-1]
		return max(self.sub_max_donation(input_list_top),self.sub_max_donation(input_list_bottom))

if __name__ == "__main__":

	input_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
	input_list1 = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
	input_list2 = [10, 3, 2, 5, 7, 8]
	maxDo = BadNeighbors(input_list2)
	print maxDo.max_donation()