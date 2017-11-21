#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午2:07
# @Author  : Yanheng Wei
# @Site    : Haizhi
# @File    : lis.py
# @Software: PyCharm


def lis(a, n):
	d = [None]*n
	length = 1
	for i in range(n):
		d[i] = 1
		for j in range(i):
			if a[j] < a[i] and d[j]+1 > d[i]:
				d[i] = d[j]+1
		if length < d[i]:
			length = d[i]
	return length


if __name__ == "__main__":
	a = [5, 3, 4, 8, 6, 7]
	print lis(a, 6)
