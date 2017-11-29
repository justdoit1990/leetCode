#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 上午11:01
# @Author  : Yanheng Wei
# @File    : FlowerGarden.py
# @Software: PyCharm


class FlowerGarden(object):

	def getOrdering(self, height, bloom, wilt):
		flowers = zip(height, bloom, wilt)
		flowers.sort()
		def flowersOverlap(f1, f2):
			# Overlap if each blooms before the other wilts.
			return f2[1] <= f1[2] and f1[1] <= f2[2]

		rows = []
		for flower in flowers:
			rowIndex = len(rows)
			# print rowIndex
			# Start at the back and march forward as long as
			# `flower` wouldn't block any flowers behind it.
			while rowIndex > 0 and not flowersOverlap(flower, rows[rowIndex - 1]):
				rowIndex -= 1
			rows[rowIndex:rowIndex] = [flower]

		return [flower[0] for flower in rows]





if __name__ == "__main__":
	height = [1, 2, 3, 4, 5, 6]
	bloom = [1, 3, 1, 3, 1, 3]
	wilt = [2, 4, 2, 4, 2, 4]

	lg = FlowerGarden()
	print lg.getOrdering(height, bloom, wilt)

