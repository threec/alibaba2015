# coding:utf-8

import sklearn,pandas
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV


if __name__ == '__main__':
	data = pandas.read_csv('data_train.csv')
	X=np.log(0.3+data[['user_item_lastday_count']].as_matrix())
	Y=data['buy'].as_matrix()

	data_test = pandas.read_csv('data_test.csv')
	X_test = np.log(0.3+data_test[['user_item_lastday_count']])
	Y_test = data_test['buy']

	parms = {
	'C':np.logspace(-6,1,10),
	'class_weight':[{0:1,1:2},{0:1,1:10},{0:1,1:30},{0:1,1:100},{0:1,1:300},{0:1,1:1000}]
	}
	lr = LogisticRegression()
	clf = GridSearchCV(lr, parms, scoring='f1', n_jobs=16)

	clf.fit(X,Y)
	
	import pickle
	f = open('model0.model','wb')
	pickle.dump(clf, f)
	f.close()
	
	print clf
	print 'best score', clf.best_score_
	print 'best parms', clf.best_params_
	
	pred = clf.predict(X_test)
	print 'test f1 score', f1_score(Y_test, pred)

