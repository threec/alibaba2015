# coding:utf-8
import pandas, util, os, pickle
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
def GetGeoTree():
	# print os.path.exists('geotree')
	if os.path.exists('geotree'):
		tree = util.load_obj('geotree')
		return tree
		
	geo_hash = pandas.read_csv('tianchi_mobile_recommend_train_user.csv.subset.csv')
	geo_hash = geo_hash.dropna()
	geo_count=dict()
	for i in geo_hash['user_geohash']:
		if i[:1] in ['9','m','f']:
			util.IncDict(geo_count, i[:2])
			if i[:2] in ['9q', '9r', '99', '95', '94', '97', '96', 'mt', 'ff']:
				util.IncDict(geo_count, i[:3])
		util.IncDict(geo_count, i[:1])
	geo_tree = {i:geo_count[i] for i in geo_count.keys() if geo_count[i]>1e5 or len(i)==1}
	util.save_obj(geo_tree, 'geotree')
	
	return geo_tree
def GeoMatch(geo_hash, geo_list):
	geo_set = set(geo_list)
	max_len = max([len(i) for i in geo_set])
	for i in range(max_len,0,-1):
		if geo_hash[:i] in geo_set:
			return geo_hash[:i]

def GeoSamePrefixLen(geo1, geo2):
	assert len(geo1)==len(geo2)
	L = len(geo1)
	for i in range(L):
		if geo1[i]!=geo2[i]:
			break
			
	return i 
	
def GeoDistance(geo1, geo2):
	return len(geo1) - GeoSamePrefixLen(geo1, geo2)

def UserItemGeoDistance(user_geos, item_geos):  # 用户geo集合和物品geo集合的距离，算最短的那个
	d = []
	for i in user_geos:
		for j in item_geos:
			d.append( GeoDistance(i, j) )
	return min(d)


	
	
if __name__ == '__main__':
	GetItemGeo()