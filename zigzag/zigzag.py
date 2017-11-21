#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午3:15
# @Author  : Yanheng Wei
# @File    : zigzag.py
# @Software: PyCharm

'''
sub_problem: 前i个数的最长zigzag，定义其状态为d[i]，这里需要注意的根据序列的增长率，有两种序列状态，增序列和减序列，如果当前数字比前一个数字大，此时该序列为增序列，反之，则为减序列。
状态转移：由于序列的有两种状态，那么状态转移需要根据两种状态分别进行状态转移，最终判定得出最长子序列。

'''


def max_zigzag(zigzag):
	try:
		assert zigzag
	except:
		return 0
	up = [1]*len(zigzag)  # length of the max up zigzag sequence in i-th number
	down = [1]*len(zigzag)  # length of the max down zigzag sequence in i-th number
	max_length = 1
	for i in range(1, len(zigzag)):
		maxup = 0   # the length of the current up sequence
		maxdown = 0  # the length of the current down sequence
		for j in range(i):
			if zigzag[i] > zigzag[j] and maxup<down[j]: # now i-th number bigger than j-th number ,the last zigzag sequence shoulb be down sequence
				maxup = down[j]
			if zigzag[i] < zigzag[j] and maxdown<up[j]:
				maxdown = up[j]
		up[i] = maxup+1
		down[i] = maxdown+1
		max_length_i = max(up[i], down[i])
		max_length = max(max_length, max_length_i)

	return max_length

if __name__ == "__main__":
	z = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
	z1 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
	# result: 1, 17, 10, 13, 10, 16, 8
	print 'the length of the max zigzag subsequence is {}'.format(max_zigzag(z1))









