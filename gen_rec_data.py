# coding:utf-8
# rec for user item
import sklearn,pandas,csv
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import f1_score

import pickle

# load model
f = open('model2.model','rb')
clf = pickle.load(f)
f.close()

# load need to be recommanded item
items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
items = set(items['item_id'])

f = open('feature_total.csv.subset.csv','rb')
fr = csv.reader(f, delimiter=',')


fo = open('submit.csv', 'wb')
fw = csv.writer(fo, delimiter=',')
fw.writerow(['user_id','item_id'])

fr.next()
i = 0
for row in fr:
	uid = int(row[0])
	tid = int(row[1])
	
	if clf.predict(np.log(0.3+np.array([float(row[x]) for x in [3,2]])))==1 and tid in items:
		print uid,tid
		fw.writerow([uid, tid])
	i = i + 1
	if i%100000==0:
		print 'processed %d row!' % i
fo.close()
f.close()

	