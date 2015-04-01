# coding:utf-8
# rec for user item
import sklearn,pandas,csv
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import f1_score

import pickle,sys

if len(sys.argv)==2:
	fout = sys.argv[1]
else:
	fout = 'submit.csv'

# load model
import model1 as model

clf = model.GetModel()

# load need to be recommanded item
items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
items = set(items['item_id'])


block_size = 100000
fr = pandas.read_csv('feature_total.csv.subset.csv', iterator=True, chunksize=block_size)


fo = open(fout, 'wb')
fw = csv.writer(fo, delimiter=',')
fw.writerow(['user_id','item_id'])

i = 0
for data in fr:
	
	
	X = model.GetFeature(data)
	Y = clf.predict(X)
	
	for idx in range(len(data)):
		uid = data['user_id'][idx]
		tid = data['item_id'][idx]
		if tid in items and Y[idx]==1:
			print uid,tid
			fw.writerow([uid, tid])
	i = i + block_size
	
	print 'processed %d row!' % i
	
fo.close()

	