#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 上午10:12
# @Author  : Yanheng Wei
# @File    : lps_fierce.py
# @Software: PyCharm


class LPS(object):

	def __init__(self, s):
		self.s = s

	def lps_detection(self):

		try:
			assert self.s
		except:
			return 0

		lps_length = 1
		for i in range(len(self.s)-1):
			for j in range(len(self.s)-1, i, -1):
				if self.s[i]==self.s[j]:
					is_lps = True
					temp_i = i
					temp_j = j
					for temp in range(1, temp_j-temp_i):
						if self.s[i+temp] != self.s[j-temp]:
							is_lps = not is_lps
							break
					if is_lps and lps_length < j-i+1:
						lps_length = j-i+1
		return lps_length

if __name__ == "__main__":
	s = "abbacdeedc"
	s = ''
	lps_ob = LPS(s)
	print lps_ob.lps_detection()