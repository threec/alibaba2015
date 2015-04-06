# coding:utf-8
import pandas
import numpy as np


def AvgData(fn, log=False):
	block_size = 100000
	fr = pandas.read_csv(fn, iterator=True, chunksize=block_size)

	avg = None
	nrows = 0
	
	rows = 0 
	for data in fr:
		nrows = nrows + len(data)
		rows = rows + np.sum( ~ pandas.isnull(data))
		if log:
			data = np.log(data)
		if avg is None:
			avg = np.sum(data)
		else:
			avg = avg + np.sum(data)
			
		print 'sum %d rows.' % nrows
	avg = avg / rows
	if log:
		return np.exp(avg)
	return avg

if __name__ == '__main__':
	print AvgData('feature10.csv', True)
