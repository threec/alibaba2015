# coding:utf-8
import pandas


def GetRecItems():
	items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
	items = set(items['item_id'])
	return items
	
