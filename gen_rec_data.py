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
import model2 as model

clf = model.GetModel()

# load need to be recommanded item
items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
items = set(items['item_id'])

f = open('feature_total.csv.subset.csv','rb')
fr = csv.reader(f, delimiter=',')


fo = open(fout, 'wb')
fw = csv.writer(fo, delimiter=',')
fw.writerow(['user_id','item_id'])

header = fr.next()
header_dict = dict()
for i in range(len(header)):
	header_dict[header[i]] = i 

i = 0
for row in fr:
	uid = int(row[0])
	tid = int(row[1])
	
	X = model.GetFeature(row, header_dict = header_dict)
	
	if tid in items and clf.predict(X)==1:
		print uid,tid
		fw.writerow([uid, tid])
	i = i + 1
	if i%100000==0:
		print 'processed %d row!' % i
fo.close()
f.close()

	