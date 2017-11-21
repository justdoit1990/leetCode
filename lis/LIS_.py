#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 下午12:08
# @Author  : Yanheng Wei
# @File    : LIS_.py
# @Software: PyCharm

def lis(ls):
	d = [1]*len(ls)
	max_length = 1
	for i in range(len(ls)):
		for j in range(i):
			if ls[i] > ls[j] and d[i] < d[j]+1:
				d[i] = d[j] + 1
		if max_length < d[i]:
			max_length = d[i]
	return max_length


if __name__ == "__main__":
	a = [5, 3, 4, 8, 6, 7]
	print lis(a)