#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 上午11:04
# @Author  : Yanheng Wei
# @File    : lps_dynamic.py
# @Software: PyCharm


class Solution(object):

	def isLsp(self, s, i, j):
		is_lps = True
		temp_i = i
		temp_j = j
		for temp in range(0, temp_j - temp_i):
			if s[i + temp] != s[j - temp]:
				is_lps = not is_lps
				break
		return is_lps

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		try:
			assert s
		except:
			return 0
		start = 0
		end = 0
		lps_length = 1
		# d = [1]*len(s)  # the length of the lsp begin with i-th char in s
		for i in range(len(s)):
			for j in range(end+1, len(s)):
				if s[i] == s[j] and j-i+1 > lps_length and self.isLsp(s, i, j):
					lps_length = j-i+1
					start = i
					end = j

		return start, end, s[start:end+1]

if __name__ == "__main__":
	s = 'abbacdefedc'
	slu_ob = Solution()
	print slu_ob.longestPalindrome(s)




