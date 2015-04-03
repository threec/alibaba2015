# coding:utf-8
'''
对数据集采样
'''

import pandas,sys
import numpy as np


if len(sys.argv)!=2:
	mode = 'train'
else:
	mode = sys.argv[1]

np.random.seed(44)

block_size = 100000
reader = pandas.read_csv('data.csv', iterator=True, chunksize=block_size)

header = True
mod = 'w'
nrows = 0
trows = 0
rows = 0
for data in reader:
	if mode=='train':
		idx = (data['buy']==1) | (np.random.rand(len(data))<.02) # 0.02
		fname = 'data.train.csv'
	else:
		idx = (np.random.rand(len(data))<0.02) 
		fname = 'data.test.csv'
	
	data[idx].to_csv(fname, mode=mod, header = header,index = False)
	header = False
	mod = 'a'
	
	nrows = np.sum(idx) + nrows
	trows = np.sum(data['buy'][idx]==1) + trows
	rows = rows + len(data)
	print 'process %d rows!' % rows
	# print data.head()
	
print 'sample %d rows, positive %d rows.' % (nrows, trows)