#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 下午4:51
# @Author  : Yanheng Wei
# @File    : AvoidRoads.py
# @Software: PyCharm

import numpy as np

class AovidRoads(object):

	def numWays(self, height, weight, bad):

		num_way = np.zeros((height+1, weight+1))

		num_way[0][0] = 1

		# print num_way

		for i in range(height+1):
			for j in range(weight+1):
				if ((i, j) in bad and (i-1, j) in bad) and ((i, j) in bad and (i, j-1) in bad):
					num_way[i][j] = 0
				elif (i, j) in bad and (i-1, j) in bad:
					# print 's'
					num_way[i][j] += num_way[i][j-1]
				elif (i, j) in bad and (i, j-1) in bad:
					# print 's'
					num_way[i][j] += num_way[i-1][j]
				else:
					# print i,j
					num_way[i][j] += num_way[i][j-1]+num_way[i-1][j]

		return num_way[-1][-1]

if __name__ == "__main__":
	ar = AovidRoads()
	print ar.numWays(6, 6, [(0,0),(1,0),(6,6),(5,6)])
	# print ar.numWays(6,6,[None])

