# coding:utf-8
'''
usage: select_feature.py model0
'''
import sys,util
import numpy as np

if len(sys.argv)!=2:
	print __doc__
model = util.load_model_from_name(sys.argv[1])
clf = model.GetModel()
X,Y = model.GetData()
feature_names = X.keys()

for i in range(len(feature_names)):
	if np.abs(clf.best_estimator_.coef_[0][i])>1e-4:
		print '"%s",\n' % feature_names[i],
