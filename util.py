# coding:utf-8
# util
import imp

def load_model_from_name(name):
	
	fp, pathname, description = imp.find_module(name)
	return imp.load_module('model5', fp, pathname, description)