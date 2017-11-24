#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 下午2:26
# @Author  : Yanheng Wei
# @File    : LPS_dynamic_n.py
# @Software: PyCharm


class Solution(object):
# 动态规划方法解决LPS问题

	def longestPalindrome(self, s):

		try:
			assert s
		except:
			return None

		start = 0
		end = 0
		for i in range(len(s)-1):
			if s[i]==s[i+1]:
				start_i = i
				end_i = i+1
				while(start_i>=0 and end_i<len(s) and s[start_i]==s[end_i]):
					if end-start < end_i - start_i:
						start = start_i
						end = end_i
						start_i-=1
						end_i+=1
			else:
				start_i = i-1
				end_i = i+1
				while (start_i > 0 and end_i < len(s) and s[start_i] == s[end_i]):
					if end - start < end_i - start_i:
						start = start_i
						end = end_i
						start_i -= 1
						end_i += 1
		return start, end, s[start:end+1]

if __name__ == "__main__":
	# s = 'abbacdefedc'
	s = 'bb'
	slu_ob = Solution()
	print slu_ob.longestPalindrome(s)


