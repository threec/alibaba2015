# coding:utf-8

import sklearn,pandas, pickle
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV

def GetData():
	
	data = pandas.read_csv('data.csv.subset.csv')
	
	
	X=GetFeature(data)
	
	
	Y=data['buy']
	
	return X, Y
	
def GetFeature(data):
	data['item_to_cat_rate'] = data['user_item_lastday_count'] / (1 + data['user_cat_lastday_count'])
	data['user_item_lastday_count'] = np.log(0.3+data['user_item_lastday_count'])
	
	X=data[['user_item_lastday_count','item_to_cat_rate']]
	
	return X

		
def GetModel():
	f = open('model3.model','rb')
	clf = pickle.load(f)
	f.close()
	return clf

if __name__ == '__main__':
	
	X, Y = GetData()

	parms = {
	'C':np.logspace(-6,0,10),
	#'class_weight':[{0:1,1:200}] #[{0:1,1:50},{0:1,1:70},{0:1,1:85},{0:1,1:100},{0:1,1:120},{0:1,1:150}]
	}
	lr = LinearSVC(penalty="l1")
	clf = GridSearchCV(lr, parms, scoring='f1', n_jobs=10)

	clf.fit(X,Y)
	
	import pickle
	f = open('model3.model','wb')
	pickle.dump(clf, f)
	f.close()
	
	pred = clf.predict(X)
	
	from summary import summary,clf_summary
	clf_summary(clf)
	summary(Y, pred)
	
	
	
	


