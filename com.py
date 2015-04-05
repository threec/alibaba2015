# coding:utf-8
import pandas
import numpy as np


def GetRecItems():
	items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
	items = set(items['item_id'])
	return items
	
def GetItemGeo():
	items = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
	item_geo = dict()
	for i in range(len(items)):
		tid = items['item_id'][i]
		geo = items['item_geohash'][i]
		
		# print geo, geo is not np.nan
		if geo is not np.nan:
			if tid not in item_geo:
				item_geo[tid] = set()
			
			item_geo[tid].add(geo)
	return item_geo
	
if __name__ == '__main__':
	GetItemGeo()