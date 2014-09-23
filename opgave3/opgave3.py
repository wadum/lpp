#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

def readFile():
	array = []
	with open("experimentalResults.txt", "r") as file:
		for line in file:
			(a,b) = line.split(" ")
			array.append([float(a), float(b)])
	return array

def printAverage(averages):
	with open("results.txt", "w") as file:
		file.write(str(averages))

def getAverageRowArray(array):
	[a,b] = reduce(lambda x, y:[x[0]+y[0],x[1]+y[1]], array, [0,0])
	return [a/len(array), b/len(array)]

def getAverageColumnArray(array):
	return [sum(array[0])/len(array[0]), sum(array[1])/len(array[1])]

def transformarray(array):
	[a,b] =  zip(*array)
	return [list(a), list(b)]

if __name__ == '__main__':
	row_list = readFile()
	averageRowList = getAverageRowArray(row_list)
	printAverage(averageRowList)

	column_list = transformarray(row_list)
	averageColumnList = getAverageColumnArray(column_list)

	print column_list[1][25]

	column_dict = {'column0': column_list[0], 'column1': column_list[1]}

	print column_dict['column1'][25]