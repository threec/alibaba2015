# coding:utf-8
'''
利用特征 最后一天对物品点击数，最后一天对品牌点击数， 用户转化率，商品最后一天热门程度
'''
import sklearn,pandas, pickle, os
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV

def GetData():
	
	data = pandas.read_csv('data.train.csv')
	
	Y=data['buy'].as_matrix()
	
	X=GetFeature(data)
	
	
	
	
	#rand = np.random.rand(len(Y))<0.0001
	#idx = (Y==1) | ((Y==0) & rand)
	
	#X = X[idx]
	#Y = Y[idx]

	
	return X, Y
	
def GetFeature(data):
	X = np.log(0.3+data[[i for i in data.columns if i not in ['user_id','item_id','buy']]].as_matrix())
	
	
	return X

		
def GetModel():
	name = os.path.basename(__file__)
	name = name[:name.index('.')]
	f = open('%s.model' % name,'rb')
	clf = pickle.load(f)
	f.close()
	return clf

def TestModel():
	clf = GetModel()
	
	print '===== for test ====='
	
	block_size = 100000
	reader = pandas.read_csv('data.csv', iterator=True, chunksize=block_size)
	TP = 0.
	TN = 0.
	FP = 0.
	FN = 0.
	for data in reader:
		X_test = GetFeature(data)
		Y_test = data['buy'].as_matrix()
		pred = clf.predict(X_test)
		
		TP = TP + np.sum(Y_test * pred)
		TN = TN + np.sum((1-Y_test) * pred)
		FP = FP + np.sum(Y_test * (1 - pred))
		FN = FN + np.sum((1-Y_test) * (1 - pred))
	
	print ' \tF\tT'
	print 'N\t%d\t%d' % (FN, TN)
	print 'P\t%d\t%d' % (FP, TP)
	
	P = TP/(TP + TN)
	R = TP/(TP + FP)
	
	F1 = 2*P*R/(P+R)
	print 'F1\tP\tR'
	print '%.2f\t%.2f\t%.2f' % (F1*100, P*100, R*100)
	# print clf.grid_scores_
	return TP,TN,FP,FN
	
	
if __name__ == '__main__':
	
	X, Y = GetData()

	parms = {
	'C':np.logspace(-6,3,20),
	}
	lr = LogisticRegression(penalty='l1')
	clf = GridSearchCV(lr, parms, scoring='f1', n_jobs=20)

	clf.fit(X,Y)
	
	import pickle
	f = open(os.path.basename(__file__).replace('.py','.model'),'wb')
	pickle.dump(clf, f)
	f.close()
	
	
	
	pred = clf.predict(X)
	from summary import summary,clf_summary
	clf_summary(clf)
	summary(Y, pred)
	
	
	TestModel()


