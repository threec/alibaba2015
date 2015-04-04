# coding:utf-8

import csv, time,sys
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
	
	user_item_buy = dict()
	
	
	# 细化行为特征
	user_item_lastweek_click = dict()
	user_item_lastweek_star = dict()
	user_item_lastweek_add_car = dict()
	user_item_lastweek_buy = dict()
	
	user_item_halfmonth_click = dict()
	user_item_halfmonth_star = dict()
	user_item_halfmonth_add_car = dict()
	user_item_halfmonth_buy = dict()
	
	user_item_before_halfmonth_click = dict()
	user_item_before_halfmonth_star = dict()
	user_item_before_halfmonth_add_car = dict()
	user_item_before_halfmonth_buy = dict()
	
	
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
			
			diff_time = DiffTime('%s 00' % lastday, row[5]) + 24*24*3600
			
			
			
			if row[5][:10]==lastday:  # lastday
				
				pass
				
			
			if row[2] == '1': # click
				if diff_time < 6*24*3600: # lastweek
					
					IncDict(user_item_lastweek_click, utid)
				elif diff_time < 14*24*3600: # last half month
					IncDict(user_item_halfmonth_click, utid)
				else:  # before half month
					IncDict(user_item_before_halfmonth_click, utid)
			if row[2] == '2': # star
				
	
				if diff_time < 6*24*3600: # lastweek
					IncDict(user_item_lastweek_star, utid)
				elif diff_time < 14*24*3600: # last half month
					IncDict(user_item_halfmonth_star, utid)
				else:  # before half month
					IncDict(user_item_before_halfmonth_star, utid)
					
			if row[2] == '3': # add to car
				
				
				if diff_time < 6*24*3600: # lastweek
					IncDict(user_item_lastweek_add_car, utid)
				elif diff_time < 14*24*3600: # last half month
					IncDict(user_item_halfmonth_add_car, utid)
				else:  # before half month
					IncDict(user_item_before_halfmonth_add_car, utid)
					
					
			if row[2] == '4':  # buy
				
				IncDict(user_item_buy, utid)
				
				# print utid
				if diff_time < 6*24*3600: # lastweek
					IncDict(user_item_lastweek_buy, utid)
			
				elif diff_time < 14*24*3600: # last half month
					IncDict(user_item_halfmonth_buy, utid)
				else:  # before half month
					IncDict(user_item_before_halfmonth_buy, utid)
			
			
				
			i = i + 1
			if i%100000==0:
				print 'processed %d scores!' % i
				
	# user feature
	fd = open(foutput,'wb')
	fw = csv.writer(fd, delimiter=',')

	fw.writerow(['user_id', 'item_id',"user_item_buy",
		"user_item_lastweek_click", "user_item_lastweek_star", "user_item_lastweek_add_car", "user_item_lastweek_buy",
		"user_item_halfmonth_click","user_item_halfmonth_star","user_item_halfmonth_add_car","user_item_halfmonth_buy",
		"user_item_before_halfmonth_click","user_item_before_halfmonth_star","user_item_before_halfmonth_add_car","user_item_before_halfmonth_buy"
	])
	
	for key in user_items:
		uid, tid = key.split('_')
		cid = item_cat[tid]
		utid = '%s_%s' % (uid, tid)
		ucid = '%s_%s' % (uid, cid)
		
		data = [uid, tid,
			GetDict(user_item_buy, utid),
			GetDict(user_item_lastweek_click, utid),
			GetDict(user_item_lastweek_star, utid),
			GetDict(user_item_lastweek_add_car, utid),
			GetDict(user_item_lastweek_buy, utid),

			GetDict(user_item_halfmonth_click, utid),
			GetDict(user_item_halfmonth_star, utid),
			GetDict(user_item_halfmonth_add_car, utid),
			GetDict(user_item_halfmonth_buy, utid),
			GetDict(user_item_before_halfmonth_click, utid),
			GetDict(user_item_before_halfmonth_star, utid),
			GetDict(user_item_before_halfmonth_add_car, utid),
			GetDict(user_item_before_halfmonth_buy, utid),

			]
		
		fw.writerow(data)
		
	fd.close()	


if __name__ == '__main__':
	if sys.argv[1]=='train':
		GenFeature('user_action_train.csv', 'feature2.csv', lastday='2014-12-17')
	if sys.argv[1]=='submit':
		GenFeature('tianchi_mobile_recommend_train_user.csv', 'feature_total2.csv', lastday='2014-12-18')