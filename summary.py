# coding:utf-8
'''
usage summary.py modelname
'''
	
	
import sklearn,pandas
from sklearn.metrics import f1_score,precision_score,recall_score,confusion_matrix
from sklearn.linear_model import  LogisticRegression
import numpy as np 
import util, sys 

def summary(Y, pred):
	print 'F1\tP\tR'
	print '%.2f\t%.2f\t%.2f' % (f1_score(Y, pred)*100, precision_score(Y,pred)*100, recall_score(Y, pred)*100)
	
	print ''
	print ' \tF\tT'
	print 'N\t%d\t%d' % (np.sum((Y==0) & (pred==0)), np.sum((Y==0) & (pred==1)))
	print 'P\t%d\t%d' % (np.sum((Y==1) & (pred==0)), np.sum((Y==1) & (pred==1)))
	print '\n'
	
	
def clf_summary(clf, feature_names=None):
	# print clf
	print 'best score', clf.best_score_
	print 'best parms', clf.best_params_
	
	if not isinstance(clf, LogisticRegression):
		print clf.best_estimator_
		return
	
	print 'clf parms (%d features):' % len(clf.best_estimator_.coef_[0])
	if feature_names is None:
		print clf.best_estimator_.intercept_[0],
		for c in clf.best_estimator_.coef_[0]:
			print c,
		print '\n'
	else:
		print 'intercept\t%.6f' % clf.best_estimator_.intercept_[0]
		for i in range(len(clf.best_estimator_.coef_[0])):
			print '%s\t%.6f' % (feature_names[i],clf.best_estimator_.coef_[0][i])
		print '\n'
	

def TestModel(modelname):
	model = util.load_model_from_name(modelname)
	clf = model.GetModel()
	
	print '===== for test ====='
	
	block_size = 10000
	reader = pandas.read_csv('data.test.csv', iterator=True, chunksize=block_size)
	TP = 0.
	TN = 0.
	FP = 0.
	FN = 0.
	for data in reader:
		X_test = model.GetFeature(data).as_matrix()
		Y_test = data['buy'].as_matrix()
		pred = clf.predict(X_test)
		
		TP = TP + np.sum(Y_test * pred)
		TN = TN + np.sum((1-Y_test) * pred)
		FP = FP + np.sum(Y_test * (1 - pred))
		FN = FN + np.sum((1-Y_test) * (1 - pred))
	
	print ' \tF\tT'
	print 'N\t%d\t%d' % (FN, TN)
	print 'P\t%d\t%d' % (FP, TP)
	print ''
	
	P = TP/(TP + TN)
	R = TP/(TP + FP)
	
	F1 = 2*P*R/(P+R)
	print 'F1\tP\tR'
	print '%.2f\t%.2f\t%.2f' % (F1*100, P*100, R*100)
	# print clf.grid_scores_
	# return TP,TN,FP,FN
	
	print ''
	
	print '===== for online test ====='
	data = pandas.read_csv('data.onlinetest.csv')
	X = model.GetFeature(data)
	Y = data['buy']
	pred = clf.predict(X)
	summary(Y, pred)
		
	return F1,P,R
	
def SelectFeature(clf, feature_names):
	for i in range(len(feature_names)):
		if np.abs(clf.best_estimator_.coef_[0][i])>1e-4:
			print '"%s",\n' % feature_names[i],

if __name__ == '__main__':
	
	
	
	if len(sys.argv)!=2:
		print __doc__
		sys.exit()
	model = util.load_model_from_name(sys.argv[1])
	clf = model.GetModel()
	X,Y = model.GetData()
	pred = clf.predict(X)
	
	feature_names = X.columns
	
	clf_summary(clf, feature_names)
	print '\n'
	summary(Y,pred)
	
	TestModel( sys.argv[1])