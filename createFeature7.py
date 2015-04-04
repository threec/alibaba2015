# coding:utf-8

import csv, time,sys,util
import numpy as np



# 特征生成文件2

def IncDict(d, key):
	if key in d:
		d[key] = d[key] + 1
	else:
		d[key] = 1

def GetDict(d, key):
	if key in d:
		return d[key]
	else:
		return 0
def DiffTime(t1, t2):
	t1 = time.mktime(time.strptime(t1,'%Y-%m-%d %H'))
	t2 = time.mktime(time.strptime(t2,'%Y-%m-%d %H'))
	return t1 - t2
	
	
def GenFeature(finput='user_action_train.csv', foutput = 'feature.csv', lastday = '2014-12-18'):
	

	
	
	# 细化行为特征
	user_cat_lastThreeDay_click = dict()
	user_cat_lastThreeDay_star = dict()
	user_cat_lastThreeDay_add_car = dict()
	user_cat_lastThreeDay_buy = dict()
	
	user_cat_lastSixDay_click = dict()
	user_cat_lastSixDay_star = dict()
	user_cat_lastSixDay_add_car = dict()
	user_cat_lastSixDay_buy = dict()
	
	user_items = set()  # 其实是用户物品对
	item_cat = dict()

	with open(finput, 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		header = reader.next()
		print header
		
		i = 0
		for row in reader:
			uid = row[0]
			tid = row[1]
			cid = row[4]
			
			utid = '%s_%s' % (uid, tid)
			ucid = '%s_%s' % (uid, cid)
			
			user_items.add('%s_%s' % (uid,tid))
			item_cat[tid] = cid
			
			diff_time = DiffTime('%s 00' % lastday, row[5])
			
			
			
			if row[5][:10]==lastday:  # lastday
				
				pass
				
			
			if row[2] == '1': # click
				if diff_time < 3*24*3600: # last three day
					
					IncDict(user_cat_lastThreeDay_click, ucid)
				elif diff_time < 6*24*3600: # last six day
					IncDict(user_cat_lastSixDay_click, ucid)
				else:  # before six month
					pass
			if row[2] == '2': # star
				
	
				if diff_time < 3*24*3600: # last three day
					IncDict(user_cat_lastThreeDay_star, ucid)
				elif diff_time < 6*24*3600: # last six day
					IncDict(user_cat_lastSixDay_star, ucid)
				else:  # before half month
					pass
					
			if row[2] == '3': # add to car
				
				
				if diff_time < 3*24*3600: # last three day
					IncDict(user_cat_lastThreeDay_add_car, ucid)
				elif diff_time < 6*24*3600: # last six day
					IncDict(user_cat_lastSixDay_add_car, ucid)
				else:  # before half month
					pass
					
					
			if row[2] == '4':  # buy
				
				
				# print utid
				if diff_time < 3*24*3600: # last three day
					IncDict(user_cat_lastThreeDay_buy, ucid)
			
				elif diff_time < 6*24*3600: # last six day
					IncDict(user_cat_lastSixDay_buy, ucid)
				else:  # before half month
					pass
			
			
				
			i = i + 1
			if i%100000==0:
				print 'processed %d scores!' % i
				
	# user feature
	fd = open(foutput,'wb')
	fw = csv.writer(fd, delimiter=',')

	fw.writerow(['user_id', 'item_id',
		"user_cat_aveThreeDayDelta_click",
		"user_cat_aveThreeDayDelta_star",
		"user_cat_aveThreeDayDelta_add_car",
		"user_cat_aveThreeDayDelta_buy",
	])
	
	for key in user_items:
		uid, tid = key.split('_')
		cid = item_cat[tid]
		utid = '%s_%s' % (uid, tid)
		ucid = '%s_%s' % (uid, cid)
		
		data = [uid, tid,
			GetDict(user_cat_lastSixDay_click, ucid)-GetDict(user_cat_lastThreeDay_click, ucid),
			GetDict(user_cat_lastSixDay_star, ucid)-GetDict(user_cat_lastThreeDay_star, ucid),
			GetDict(user_cat_lastSixDay_add_car, ucid)-GetDict(user_cat_lastThreeDay_add_car, ucid),
			GetDict(user_cat_lastSixDay_buy, ucid)-GetDict(user_cat_lastThreeDay_buy, ucid),
			]
		
		fw.writerow(data)
		
	fd.close()	


if __name__ == '__main__':
	fid = util.file_basename_id(__file__)
	if sys.argv[1]=='train':
		GenFeature('user_action_train.csv', 'feature%d.csv' % fid, lastday='2014-12-17')
	if sys.argv[1]=='submit':
		GenFeature('tianchi_mobile_recommend_train_user.csv', 'feature_total%d.csv' % fid, lastday='2014-12-18')