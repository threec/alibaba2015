# coding:utf-8
'''
usage summary.py modelname
'''
	
	
import sklearn
from sklearn.metrics import f1_score,precision_score,recall_score,confusion_matrix
import numpy as np 

def summary(Y, pred):
	print 'F1\tP\tR'
	print '%.2f\t%.2f\t%.2f' % (f1_score(Y, pred)*100, precision_score(Y,pred)*100, recall_score(Y, pred)*100)
	
	print ''
	print ' \tF\tT'
	print 'N\t%d\t%d' % (np.sum((Y==0) & (pred==1)), np.sum((Y==0) & (pred==0)))
	print 'P\t%d\t%d' % (np.sum((Y==1) & (pred==0)), np.sum((Y==1) & (pred==1)))
	print '\n'
	
def clf_summary(clf):
	# print clf
	print 'best score', clf.best_score_
	print 'best parms', clf.best_params_
	
	print 'clf parms:',
	print clf.best_estimator_.intercept_[0],
	for c in clf.best_estimator_.coef_[0]:
		print c,
	print '\n'
		
if __name__ == '__main__':
	
	import util, sys 
	
	if len(sys.argv)!=2:
		print __doc__
		sys.exit()
	model = util.load_model_from_name(sys.argv[1])
	clf = model.GetModel()
	X,Y = model.GetData()
	pred = clf.predict(X)
	
	clf_summary(clf)
	print '\n'
	summary(Y,pred)