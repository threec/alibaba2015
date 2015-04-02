# coding:utf-8
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