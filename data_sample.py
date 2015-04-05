# coding:utf-8
'''
对数据集采样
'''

import pandas,sys
import numpy as np
from com import GetRecItems

np.random.seed(44)

block_size = 100000
reader = pandas.read_csv('data.csv', iterator=True, chunksize=block_size)

header = True
mod = 'w'
train_rows = 0
test_rows = 0
train_trows = 0
test_trows = 0
online_rows = 0
online_trows = 0
rows = 0

fname1 = 'data.train.csv'
fname2 = 'data.test.csv'
fname3 = 'data.onlinetest.csv'

items = GetRecItems()

for data in reader:
	
	spl = np.random.rand(len(data))<.6  # train : test = 6:4
	train = spl & ((data['buy']==1) | (np.random.rand(len(data))<.03)) # 0.03
	test = spl == False 
	
	onlinetest = spl == False
	for i in range(len(onlinetest)):
		if onlinetest[i] and data['item_id'][i] not in items: 
			onlinetest[i] = False
	#print train[:10]
	#print test[:10]
	#print 
	assert np.sum((train==True) & (test==True))==0
	data[train].to_csv(fname1, mode=mod, header = header,index = False)
	data[test].to_csv(fname2, mode=mod, header = header,index = False)
	data[onlinetest].to_csv(fname3, mode=mod, header = header,index = False)
	
	header = False
	mod = 'a'
	
	train_rows = np.sum(train) + train_rows
	test_rows = np.sum(test) + test_rows
	train_trows = np.sum(data['buy'][train]==1) + train_trows
	test_trows = np.sum(data['buy'][test]==1) + test_trows
	online_rows = np.sum(onlinetest) + online_rows
	online_trows = np.sum(data['buy'][onlinetest]==1) + online_trows
	rows = rows + len(data)
	print 'process %d rows!' % rows
	# print data.head()
	
print 'sample %d rows, positive %d rows for train. %d rows, positive %d rows for test. %d rows, positive %d rows for online test.' % (train_rows, train_trows, test_rows, test_trows, online_rows, online_trows)
