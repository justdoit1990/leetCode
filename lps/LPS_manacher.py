#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 下午2:26
# @Author  : Yanheng Wei
# @File    : LPS_dynamic_n.py


# manacher 算法解决LPS问题

class Solution(object):


	def longestPalindrome(self, s):

		try:
			assert s
		except:
			return None

		temp = s

		s = '#' + '#'.join(s) + '#'

		RL = [0] * len(s)
		MaxRight = 0
		pos = 0
		MaxLen = 0
		for i in range(len(s)):
			if i < MaxRight:
				RL[i] = min(RL[2 * pos - i], MaxRight - i)
			else:
				RL[i] = 1
			while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
				RL[i] += 1
			if RL[i] + i - 1 > MaxRight:
				MaxRight = RL[i] + i - 1
				pos = i
			MaxLen = max(MaxLen, RL[i])

		# print MaxLen, MaxRight
		return temp[(MaxRight/2-MaxLen)+1: MaxRight]

if __name__ == "__main__":
	# s = 'abbacdefedc'
	s = 'bb'
	slu_ob = Solution()
	print slu_ob.longestPalindrome(s)


